import shutil
from argparse import ArgumentParser, Namespace
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory

# This tool is used to generate updated PO files from updated PO template (POT) files, which are
# based on the English Markdown content.

# The Markdown content can optionally contain external shared content included using the PyMdown
# Snippets extension. To facilitate translation of the shared content, it is included as part of
# BeeWare Docs Tools, along with the associated `locales` directory containing the shared content
# POT and translated PO files. This content is then processed separately from the primary content,
# and the resulting files are stored within the `docs-tools` repo `src` directory. When BeeWare
# Docs Tools is installed into a documentation repo, it includes the shared Markdown and PO files.
# They are then made available to the other translation- and build-tools, so when they are run,
# they are able to access the translated shared content and build each translated site in a given
# language.


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("language_code", nargs="*")
    args = parser.parse_args()

    for language in args.language_code:
        if not (Path.cwd() / "docs" / "locales" / f"{language}").is_dir():
            raise RuntimeError(
                f'Language code "{language}" does not match an existing translation'
            )

    return args


def pot_to_po(
    source_po_file: Path,
    pot_file_path_root: Path,
    destination_dir: Path,
) -> None:
    """
    Run `pot2po` with the provided directories.

    :param source_po_file: The existing PO file.
    :param pot_file_path_root: The directory containing the `locales` directory, relative
        to the project root.
    :param destination_dir: The output directory for the updated PO file.
    """
    destination_dir.mkdir(parents=True)
    subprocess.run(
        [
            "pot2po",
            f"--template={source_po_file}",
            f"--input={pot_file_path_root / 'locales' / 'template' / 'translations.pot'}",
            f"--output={destination_dir}",
        ],
        check=True,
    )


def generate_po_files(docs_directory: Path) -> None:
    """
    Generate PO files from PO template (POT) files.

    :param docs_directory: The directory containing the locales directory, relative to the
        project root.

    """
    args = parse_args()

    with TemporaryDirectory() as temp_destination_dir:
        temp_destination_dir = Path(temp_destination_dir)

        for language in args.language_code:
            print(f"Processing {language} content from {docs_directory}")

            # Generates PO files from POT files into a temporary destination directory.
            pot_to_po(
                source_po_file=docs_directory
                / "locales"
                / language
                / "translations.po",
                pot_file_path_root=docs_directory,
                destination_dir=temp_destination_dir / docs_directory / language,
            )

            # Copies the updated PO file to the `docs` directory.
            shutil.copyfile(
                (temp_destination_dir / docs_directory / language / "translations.po"),
                (docs_directory / "locales" / language / "translations.po"),
            )


def main():
    # Generate primary content PO files
    generate_po_files(Path("docs"))
    # Generate shared content PO files
    generate_po_files(Path("src/beeware_docs_tools/shared_content"))


if __name__ == "__main__":
    main()
