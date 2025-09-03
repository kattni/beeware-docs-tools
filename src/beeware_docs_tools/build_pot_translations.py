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


def markdown_to_pot(source_path: Path, working_path: Path) -> None:
    """
    Run `md2po` with provided input and output directories, with `--pot` flag to
    generate PO template (POT) files.

    When invoking `md2po`:
    * `--duplicates=merge` enforces multiple copies of the same string being shown
        once with multiple locations.
    * `--timestamp` ensures that new files are only generated when there is new
    content.

    :param source_path: The source directory containing the original English
        Markdown files, and the template folder containing POT files.
    :param working_path: The directory considered `/` for the input file call.
        This ensures that the location strings are accurate in the POT and PO
        files.
    """
    # Ensure the output directory exists
    output_path = Path.cwd() / source_path / "locales/template"
    output_path.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        [
            "md2po",
            f"--input={source_path}/en",
            f"--output={output_path / 'translations.pot'}",
            "--pot",
            "--timestamp",
            "--duplicates=merge",
            "--multifile=onefile",
        ],
        check=True,
        cwd=working_path,
    )


def generate_pot_files(source_path: str) -> None:
    """
    Generate the PO template (POT) files for the content in the provided
    directory.

    :param source_path: The directory, relative to the project root, containing
        the `en` Markdown content and `locales` translation files directories.
    """
    with TemporaryDirectory() as temp_working_directory:
        temp_working_path = Path(temp_working_directory)

        (temp_working_path / source_path).parent.mkdir(parents=True, exist_ok=True)

        try:
            (temp_working_path / source_path).symlink_to(
                Path.cwd() / source_path, target_is_directory=True
            )
        except FileExistsError:
            pass

        markdown_to_pot(
            source_path=source_path,
            working_path=temp_working_path,
        )


def main():
    # Generate primary content POT files.
    generate_pot_files("docs")
    # # Generate shared content POT files.
    generate_pot_files("src/beeware_docs_tools/shared_content")


if __name__ == "__main__":
    main()
