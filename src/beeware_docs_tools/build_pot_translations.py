import subprocess
from pathlib import Path

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

SOURCE_DIR = Path.cwd()
SOURCE_DOCS_DIR = SOURCE_DIR / "docs"
SOURCE_DOCS_EN_DIR = SOURCE_DOCS_DIR / "en"
LOCAL_DOCS_DIR = Path(__file__).parent / "docs"
LOCAL_DOCS_EN_DIR = LOCAL_DOCS_DIR / "en"
LOCAL_SHARED_DIR = Path(__file__).parent / "shared_content"
DOCS_EN_DIR = Path("docs") / "en"


def markdown_to_pot(input_dir: Path, output_dir: Path) -> None:
    """
    Run `md2po` with provided input and output directories, with `--pot` flag to generate
    PO template (POT) files.

    :param input_dir: The directory containing the English Markdown files.
    :param output_dir: The output directory for the generated PO template (POT) files.

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
            "--duplicates=merge",
            "--timestamp",
        ],
        check=True,
    )


def generate_pot_files(shared_content: bool = False) -> None:
    """
    Generate the PO template (POT) files for primary or shared content.

    :param bool shared_content: True when processing shared content. Defaults to False.

    """
    # md2po sets the msgid/msgstr locations to the exact path that is provided as
    # the input. The following symlinking and subsequent cleanup is necessary for
    # the locations in the POT (and therefore the PO) files to read `docs/en` on
    # primary content and `docs/en/shared_content` on shared content.
    LOCAL_DOCS_DIR.mkdir(parents=True, exist_ok=True)

    # The second symlink relies on the first, so both must happen regardless of
    # whether primary or shared content is being processed.
    try:
        LOCAL_DOCS_EN_DIR.symlink_to(SOURCE_DOCS_EN_DIR, target_is_directory=True)
    except FileExistsError:
        pass

    if shared_content:
        try:
            (LOCAL_DOCS_EN_DIR / "shared_content").symlink_to(
                LOCAL_SHARED_DIR, target_is_directory=True
            )
        except FileExistsError:
            pass

    markdown_to_pot(
        input_dir=(
            DOCS_EN_DIR if not shared_content else DOCS_EN_DIR / "shared_content"
        ),
        output_dir=(SOURCE_DOCS_DIR if not shared_content else LOCAL_SHARED_DIR)
        / "locales"
        / "templates",
    )

    LOCAL_DOCS_EN_DIR.unlink(missing_ok=True)
    (SOURCE_DOCS_EN_DIR / "shared_content").unlink(missing_ok=True)

    (Path(__file__).parent / "docs").rmdir()


def main():
    # Generate primary content POT files.
    generate_pot_files()
    # Generate shared content POT files.
    generate_pot_files(shared_content=True)


if __name__ == "__main__":
    main()
