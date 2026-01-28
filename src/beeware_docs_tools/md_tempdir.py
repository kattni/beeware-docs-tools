from pathlib import Path
from importlib.metadata import metadata

import yaml


def load_config(project_path):
    """Load the config.yml file, and add the version_number to extra."""

    with (project_path / "docs/config.yml").open() as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)

    try:
        version = metadata(config["extra"]["package_name"])["version"]
        config["extra"]["version"] = version
    except KeyError:
        pass

    return config


def save_config(project_path, temp_md_path, config, language="en"):
    """Add the base_path to Snippets, and dump the updated copy to the temp directory"""
    # Necessary so that it's available relative to the build.

    base_path = config["markdown_extensions"]["pymdownx.snippets"].get("base_path", [])

    if language != "en":
        shared_content_path = temp_md_path.resolve() / f"shared_content/{language}"
    else:
        shared_content_path = (Path(__file__).parent / "shared_content/en").resolve()

    base_path.append(str(shared_content_path))
    config["markdown_extensions"]["pymdownx.snippets"]["base_path"] = base_path
    config["plugins"]["macros"]["include_dir"] = str(shared_content_path)

    with (temp_md_path / "config.yml").open("w", encoding="utf-8") as config_f:
        yaml.dump(config, config_f)

    # Build the the language configuration into the temp directory. docs_dir and
    # INHERIT paths are relative, so to build translations successfully while
    # allowing English to build on its own, files must be available relative to
    # the build. For the main website, we also need to generate a translated
    # `nav` configuration.
    if language != "en" and "nav" in config:
        mkdocs_config = yaml.load(
            (project_path / f"docs/mkdocs.{language}.yml").read_text(),
            Loader=yaml.SafeLoader,
        )

        translated_nav = []
        for en_content, translated in zip(
            config["nav"],
            mkdocs_config["nav"],
            strict=True,
        ):
            translated_nav.append(
                {translated[original]: en_content[original] for original in en_content}
            )

        mkdocs_config["nav"] = translated_nav

        with (temp_md_path / f"mkdocs.{language}.yml").open(
            "w", encoding="utf-8"
        ) as mkdocs_f:
            yaml.dump(mkdocs_config, mkdocs_f)

    else:
        # On non-website builds, and for the English build of the website, we
        # can symlink the original language configuraton.
        (temp_md_path / f"mkdocs.{language}.yml").symlink_to(
            project_path / f"docs/mkdocs.{language}.yml"
        )


def symlink_from_temp(project_path, temp_md_path, source_code, config):
    """Symlink the relevant files so that they're available in the temp dir."""
    # If source code directory or directories provided, symlink from the temp directory,
    # so it is available relative to the build.
    if source_code:
        for source in source_code:
            # If source includes subdirectories, the parent directory must be created.
            # If a single directory is provided, this will rely on `exists_ok=True` to
            # avoid failing.
            (temp_md_path / source).parent.mkdir(parents=True, exist_ok=True)
            (temp_md_path / source).symlink_to(
                project_path / source, target_is_directory=True
            )

    # Symlink the overrides directory from the temp directory, so it is available
    # relative to the build.
    (temp_md_path / "overrides").symlink_to(
        Path(__file__).parent / "overrides", target_is_directory=True
    )

    # Symlink to the macros module, if there is one.
    try:
        module_name = config["plugins"]["macros"]["module_name"]
    except KeyError:
        module_name = "main"

    macros_path = project_path / f"docs/{module_name}.py"
    symlink_path = temp_md_path / f"{module_name}.py"
    if macros_path.is_file():
        symlink_path.parent.mkdir(parents=True, exist_ok=True)
        symlink_path.symlink_to(macros_path)
