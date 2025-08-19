import subprocess
from argparse import ArgumentParser, Namespace
from pathlib import Path
from tempfile import TemporaryDirectory


SOURCE_DIR = Path.cwd()


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("language_code", nargs="*")
    parser.add_argument("--output", default=SOURCE_DIR / "_build" / "html")
    args = parser.parse_args()
    for language_code in args.language_code:
        if not (
            (SOURCE_DIR / "locales" / f"{language_code}").is_dir()
            or language_code == "en"
        ):
            raise RuntimeError(
                f'Language code "{language_code}" does not match an existing translation'
            )

    return args


def generate_translated_md(
    input_dir: Path, template_dir: Path, output_dir: Path
) -> None:
    subprocess.run(
        [
            "po2md",
            f"--input={input_dir}",
            f"--template={template_dir}",
            f"--output={output_dir}",
            "--fuzzy",
        ],
        check=True,
    )


def build_docs(config_file: Path, build_dir: Path) -> None:
    subprocess.run(
        [
            "python",
            "-m",
            "mkdocs",
            "build",
            "--clean",
            "--strict",
            "--config-file",
            f"{config_file}",
            "--site-dir",
            f"{build_dir}",
        ],
        check=True,
    )


def main():
    args = parse_args()

    with TemporaryDirectory() as temp_md_directory:
        temp_md_directory = Path(temp_md_directory)

        # Symlink config file and overrides directory to temp directory, so they are
        # available relative to the build.
        (temp_md_directory / "config.yml").symlink_to(
            SOURCE_DIR / "docs" / "config.yml"
        )
        (temp_md_directory / "overrides").symlink_to(
            Path(__file__).parent / "overrides", target_is_directory=True
        )
        for language in args.language_code:
            print(f"Processing {language}")
            output_directory = temp_md_directory / language

            # Symlink language config to temp directory. docs_dir and INHERIT paths are
            # relative, so to build translations successfully while allowing English
            # to build on its own, files must be available relative to the build.
            (temp_md_directory / f"mkdocs.{language}.yml").symlink_to(
                SOURCE_DIR / "docs" / f"mkdocs.{language}.yml"
            )
            if language != "en":
                output_directory.mkdir(parents=True, exist_ok=True)
                generate_translated_md(
                    input_dir=SOURCE_DIR / "locales" / language / "LC_MESSAGES",
                    template_dir=SOURCE_DIR / "docs" / "en",
                    output_dir=temp_md_directory / language,
                )

                # If the documentation includes images or resources, they must be
                # explicitly symlinked for the relative links in the Markdown to
                # function the same way they do in the original Markdown files.
                # `images` and `resources` directories must live in `en` directory.
                if (SOURCE_DIR / "docs" / "en" / "images").is_dir():
                    (temp_md_directory / language / "images").symlink_to(
                        SOURCE_DIR / "docs" / "en" / "images",
                        target_is_directory=True,
                    )
                if (SOURCE_DIR / "docs" / "en" / "resources").is_dir():
                    (temp_md_directory / language / "resources").symlink_to(
                        SOURCE_DIR / "docs" / "en" / "resources",
                        target_is_directory=True,
                    )
            else:
                # Symlink English Markdown files and spelling_wordlist for en build.
                (temp_md_directory / "en").symlink_to(
                    SOURCE_DIR / "docs" / "en", target_is_directory=True
                )
                (temp_md_directory / "spelling_wordlist").symlink_to(
                    SOURCE_DIR / "docs" / "spelling_wordlist"
                )

            config_location = temp_md_directory / f"mkdocs.{language}.yml"
            output = Path(args.output).resolve()
            build_docs(
                config_file=config_location,
                build_dir=output
                if (len(args.language_code) == 1)
                else (output / language),
            )


if __name__ == "__main__":
    main()
