import os
import textwrap
from argparse import ArgumentParser, Namespace
from pathlib import Path

import deepl
import polib


def parse_args() -> Namespace:
    parser = ArgumentParser(
        description=(
            "Update translations for a documentation set. Uses the DeepL API "
            "to provide a machine translation of every untranslated string "
            "for the given language. Machine translations are marked 'fuzzy' "
            "as an indicator that additional translation work is required."
        )
    )
    parser.add_argument(
        "--soft-fail",
        action="store_true",
        help="Fail without raising an error if the API key cannot be found",
    )
    parser.add_argument(
        "--input",
        dest="input_dir",
        action="append",
        help=(
            "The path to a documentation set. The provided location should "
            "contain a 'locales' subdirectory"
        ),
    )
    parser.add_argument("language_code", nargs="+", help="The language to translate.")

    args = parser.parse_args()

    for dir in args.input_dir:
        input_path = Path(dir)
        if not (input_path / "locales").is_dir():
            raise RuntimeError(f"Input path {dir} should contain a 'locales' directory")

    for language_code in args.language_code:
        if not (input_path / "locales" / language_code).exists():
            raise RuntimeError(
                f'A translation for "{language_code}" does not exist in {dir}'
            )

    return args


def translate(client, path, language):
    print(f"  {language}: Translate {path.relative_to(Path.cwd())}")
    # 78 is 80, allowing for an open and closing "
    po = polib.pofile(path, wrapwidth=78)
    for entry in po.untranslated_entries():
        print(
            f"    {language}:{path.name} "
            f"| {entry.msgid[:50]}{'...' if len(entry.msgid) > 50 else ''}"
        )
        translated = client.translate_text(entry.msgid, target_lang=language)
        entry.msgstr = translated.text
        entry.fuzzy = True

    po.save(path)


def main():
    args = parse_args()
    try:
        client = deepl.DeepLClient(os.environ["DEEPL_API_KEY"])
    except KeyError:
        if args.soft_fail:
            print(
                textwrap.dedent("""
                    *******************************************************
                    *         WARNING: No DeepL API key found.            *
                    *******************************************************

                        Machine translations will be skipped. If you want
                        to update machine translations, ensure that the
                        environment variable DEEPL_API_KEY has been set.

                    *******************************************************
                    """)
            )
        else:
            raise RuntimeError(
                "No DeepL API key found; set the DEEPL_API_KEY environment variable."
            ) from None
    else:
        for language in args.language_code:
            print(f"Translating {language}:")
            for dir in args.input_dir:
                for path in (Path(dir) / "locales" / language).glob("**/*.po"):
                    translate(client, path, language)
                if (lang_po := Path(dir) / "locales" / f"{language}.po").is_file():
                    translate(client, lang_po, language)


if __name__ == "__main__":
    main()
