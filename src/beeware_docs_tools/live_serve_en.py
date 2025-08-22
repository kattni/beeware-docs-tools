import subprocess
from argparse import ArgumentParser, Namespace
from pathlib import Path
import yaml
from setuptools_scm import get_version
from tempfile import TemporaryDirectory

# The theme overrides directory in config.yml is relative to the docs directory.
# Therefore, the live build expects there to be an overrides directory in the
# local docs directory. This script symlinks all the necessary directories and
# config files to a temp directory and serves the live build from the temp directory.

SOURCE_DIR = Path.cwd()

version = get_version(relative_to=SOURCE_DIR / "tox.ini")


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("watch_directory", nargs="*")
    parser.add_argument("--build-with-errors", action="store_true")
    args = parser.parse_args()

    return args


def serve_docs(config_location) -> None:
    args = parse_args()

    serve_command = [
        "python",
        "-m",
        "mkdocs",
        "serve",
        "--clean",
        "--config-file",
        f"{config_location}",
        "--watch",
        "docs",
    ]

    if not args.build_with_errors:
        serve_command.extend(["--strict"])

    if args.watch_directory:
        for directory in args.watch_directory:
            serve_command.extend(["--watch", directory])

    subprocess.run(
        serve_command,
        check=True,
    )


def main():
    with TemporaryDirectory() as temp_md_directory:
        temp_md_directory = Path(temp_md_directory)

        config_file = yaml.load(
            open(SOURCE_DIR / "docs" / "config.yml"), Loader=yaml.SafeLoader
        )
        config_file["extra"].update({"version": f"{version}"})

        with (temp_md_directory / "config.yml").open(
            "w", encoding="utf-8"
        ) as config_temp:
            yaml.dump(config_file, config_temp)

        (temp_md_directory / "mkdocs.en.yml").symlink_to(
            SOURCE_DIR / "docs" / "mkdocs.en.yml"
        )
        (temp_md_directory / "overrides").symlink_to(
            Path(__file__).parent / "overrides", target_is_directory=True
        )
        (temp_md_directory / "en").symlink_to(
            SOURCE_DIR / "docs" / "en", target_is_directory=True
        )

        serve_docs(config_location=(temp_md_directory / "mkdocs.en.yml"))


if __name__ == "__main__":
    main()
