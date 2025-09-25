import subprocess
from argparse import ArgumentParser, Namespace
from importlib.metadata import metadata
from pathlib import Path
from tempfile import TemporaryDirectory

import yaml

# The theme overrides directory in config.yml is relative to the docs directory.
# Therefore, the live build expects there to be an overrides directory in the
# local docs directory. This script symlinks all the necessary directories and
# config files to a temp directory and serves the live build from the temp
# directory.

PROJECT_PATH = Path.cwd()


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("watch_directory", nargs="*")
    parser.add_argument("--build-with-warnings", action="store_true")
    parser.add_argument("--source-code", action="append")
    args = parser.parse_args()

    return args


def serve_docs(output_path) -> None:
    args = parse_args()

    serve_command = [
        "python",
        "-m",
        "mkdocs",
        "serve",
        "--clean",
        "--config-file",
        f"{output_path / 'mkdocs.en.yml'}",
        "--watch",
        "docs",
    ]

    if not args.build_with_warnings:
        serve_command.extend(["--strict"])

    if args.watch_directory:
        for directory in args.watch_directory:
            serve_command.extend(["--watch", directory])

    subprocess.run(
        serve_command,
        check=True,
    )


def main():
    args = parse_args()

    with TemporaryDirectory() as temp_md_directory:
        temp_md_directory = Path(temp_md_directory)

        if args.source_code:
            for directory in args.source_code:
                # If `directory` includes subdirectories, the parent directory
                # or directories must be created. If a single directory is
                # provided, this will rely on `exists_ok=True` to avoid failing.
                Path(temp_md_directory / directory).parent.mkdir(
                    parents=True, exist_ok=True
                )
                (temp_md_directory / directory).symlink_to(
                    PROJECT_PATH / directory, target_is_directory=True
                )

        with (PROJECT_PATH / "docs/config.yml").open() as f:
            config_file = yaml.load(f, Loader=yaml.SafeLoader)

        try:
            version = metadata(config_file["extra"]["package_name"])["version"]
            config_file["extra"]["version"] = version
        except KeyError:
            pass

        base_path = config_file["markdown_extensions"]["pymdownx.snippets"].get(
            "base_path", []
        )

        shared_content_path = (Path(__file__).parent / "shared_content/en").resolve()
        base_path.append(str(shared_content_path))

        config_file["markdown_extensions"]["pymdownx.snippets"]["base_path"] = base_path

        with (temp_md_directory / "config.yml").open(
            "w", encoding="utf-8"
        ) as config_temp:
            yaml.dump(config_file, config_temp)

        (temp_md_directory / "mkdocs.en.yml").symlink_to(
            PROJECT_PATH / "docs/mkdocs.en.yml"
        )
        (temp_md_directory / "overrides").symlink_to(
            Path(__file__).parent / "overrides",
            target_is_directory=True,
        )
        (temp_md_directory / "en").symlink_to(
            PROJECT_PATH / "docs/en",
            target_is_directory=True,
        )

        serve_docs(temp_md_directory)


if __name__ == "__main__":
    main()
