import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

# This tool is used to generate PO template (POT) files from English Markdown content.

# The Markdown content can optionally contain external shared content included using the PyMdown
# Snippets extension. To facilitate translation of the shared content, it is included as part of
# BeeWare Docs Tools, along with the associated `locales` directory containing the shared content
# POT and translated PO files. This content is then processed separately from the primary content,
# and the resulting files are stored within the `docs-tools` repo `src` directory. When BeeWare
# Docs Tools is installed into a documentation repo, it includes the shared Markdown and PO files.
# They are then made available to the other translation- and build-tools, so when they are run,
# they are able to access the translated shared content and build each translated site in a given
# language.


def markdown_to_pot(input_dir: Path, output_dir: Path, working_dir: Path) -> None:
    """
    Run `md2po` with provided input and output directories, with `--pot` flag to generate
    PO template (POT) files.

    :param input_dir: The directory containing the English Markdown files.
    :param output_dir: The output directory for the generated PO template (POT) files.
    :param working_dir: The directory considered `/` for the input file call. This ensures
                        that the location strings are accurate in the POT and PO files.

    `--duplicates=merge` enforces multiple copies of the same string being shown
        once with multiple locations.
    `--timestamp` ensures that new files are only generated when there is new content.
    """
    subprocess.run(
        [
            "md2po",
            f"--input={input_dir}",
            f"--output={output_dir}",
            "--pot",
            "--timestamp",
            "--duplicates=merge",
            "--multifile=onefile",
        ],
        check=True,
        cwd=working_dir,
    )


def generate_pot_files(docs_directory: Path) -> None:
    """
    Generate the PO template (POT) files for the content in the provided directory.

    :param docs_directory: The directory, relative to the project root, containing the `en`
                            Markdown content and `locales` translation files directories.
    """
    with TemporaryDirectory() as temp_working_directory:
        temp_working_directory = Path(temp_working_directory)

        (temp_working_directory / docs_directory).parent.mkdir(
            parents=True, exist_ok=True
        )

        try:
            (temp_working_directory / docs_directory).symlink_to(
                Path.cwd() / docs_directory, target_is_directory=True
            )
        except FileExistsError:
            pass

        markdown_to_pot(
            input_dir=(docs_directory / "en"),
            output_dir=(docs_directory / "locales" / "template" / "translations.pot"),
            working_dir=temp_working_directory,
        )


def main():
    # Generate primary content POT files.
    generate_pot_files(Path("docs"))
    # # Generate shared content POT files.
    generate_pot_files(Path("src/beeware_docs_tools/shared_content"))


if __name__ == "__main__":
    main()
