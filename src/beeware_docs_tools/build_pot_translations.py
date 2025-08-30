import subprocess
from argparse import ArgumentParser, Namespace
from pathlib import Path


SOURCE_DIR = Path.cwd()


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("language_code", nargs="*")
    args = parser.parse_args()
    for language_code in args.language_code:
        if not (
            (SOURCE_DIR / "docs" / "locales" / f"{language_code}").is_dir()
            or language_code == "en"
        ):
            raise RuntimeError(
                f'Language code "{language_code}" does not match an existing translation'
            )

    return args


def generate_translated_pot_files(input_dir: Path, output_dir: Path) -> None:
    subprocess.run(
        [
            "md2po",
            f"--input={input_dir}",
            f"--output={output_dir}",
            "--pot",
            "--duplicates=merge",
        ],
        check=True,
    )


def main():
    args = parse_args()

    for language in args.language_code:
        print(f"Processing {language}")
        output_directory = SOURCE_DIR / "docs" / "locales" / "templates"

        if language != "en":
            output_directory.mkdir(parents=True, exist_ok=True)
            generate_translated_pot_files(
                input_dir=SOURCE_DIR / "docs" / "en",
                output_dir=output_directory,
            )
            generate_translated_pot_files(
                input_dir=Path(__file__).parent / "shared_content",
                output_dir=output_directory / "shared_content",
            )


if __name__ == "__main__":
    main()
