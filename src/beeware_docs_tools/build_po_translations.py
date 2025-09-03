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

    for language_code in args.language_code:
        if not (Path.cwd() / "docs" / "locales" / f"{language_code}").is_dir():
            raise RuntimeError(
                f'Language code "{language_code}" does not match an existing translation'
            )

    return args


def pot_to_po(source_dir: Path, template_dir: Path, destination_dir: Path) -> None:
    """
    Run `pot2po` with the provided directories.

    :param source_dir: The directory containing the existing PO files.
    :param template_dir: The directory containing the PO template (POT) files.
    :param destination_dir: The output directory for the updated PO files.
    """
    destination_dir.mkdir(parents=True)
    subprocess.run(
        [
            "pot2po",
            f"--template={source_dir}",
            f"--input={template_dir}",
            f"--output={destination_dir}",
        ],
        check=True,
    )


def generate_po_files(docs_directory: Path) -> None:
    """
    Generate PO files from PO template (POT) files.

    :param docs_directory:

    """
    args = parse_args()

    with TemporaryDirectory() as temp_destination_dir:
        temp_destination_dir = Path(temp_destination_dir)

        for language in args.language_code:
            print(f"Processing {language} content from {docs_directory}")

            # Generates PO files from POT files into a temporary destination directory.
            pot_to_po(
                source_dir=docs_directory / "locales" / Path(language),
                template_dir=docs_directory / "locales" / "template",
                destination_dir=temp_destination_dir / docs_directory / Path(language),
            )

            # Copies the contents of the temp destination directory into the final
            # destination directory.
            shutil.copytree(
                (temp_destination_dir / docs_directory / language),
                (docs_directory / "locales" / language),
                dirs_exist_ok=True,
            )


def main():
    # Generate primary content PO files
    generate_po_files(Path("docs"))
    # Generate shared content PO files
    generate_po_files(Path("src/beeware_docs_tools/shared_content"))


if __name__ == "__main__":
    main()
