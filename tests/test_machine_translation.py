import os
from unittest.mock import Mock

import polib
import pytest

from beeware_docs_tools.update_machine_translations import translate


def write_po_file(path, data):
    content = [
        """\
#
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\\n"
"Report-Msgid-Bugs-To: \\n"
"POT-Creation-Date: 2026-02-05 14:13+0800\\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n"
"Language-Team: LANGUAGE <LL@li.org>\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"X-Generator: Translate Toolkit 3.18.1\\n"
"""
    ]

    for i, input in enumerate(data):
        content.append(f"""
#: docs/en/file{i}.md:1
msgid "{input}"
msgstr ""
""")

    path.write_text("".join(content), encoding="utf-8")


def mock_translation(value):
    translated = Mock()
    translated.text = value.upper()

    return translated


@pytest.mark.parametrize(
    ("input", "translated", "output", "fuzzy"),
    [
        # Simple text
        pytest.param(
            "Hello World", "Hello World", "HELLO WORLD", True, id="simple-text"
        ),
        # Notes
        pytest.param("/// Note", None, "/// Note", False, id="note"),
        pytest.param(
            "/// Note | Windows", None, "/// Note | Windows", False, id="note-windows"
        ),
        pytest.param(
            "/// Note | macOS", None, "/// Note | macOS", False, id="note-macos"
        ),
        pytest.param(
            "/// Note | Linux", None, "/// Note | Linux", False, id="note-linux"
        ),
        pytest.param("/// Note | iOS", None, "/// Note | iOS", False, id="note-ios"),
        pytest.param(
            "/// Note | Android", None, "/// Note | Android", False, id="note-android"
        ),
        pytest.param(
            "/// Note | Other text",
            " Other text",
            "/// Note | OTHER TEXT",
            True,
            id="note-other",
        ),
        # Attributed headings
        pytest.param(
            "## Some Title { #some-title }",
            "## Some Title",
            "## SOME TITLE { #some-title }",
            True,
            id="attr-heading",
        ),
        # Complete Jinja line
        pytest.param(
            "{{ value.upper()|default:other }}",
            None,
            "{{ value.upper()|default:other }}",
            False,
            id="jinja-value",
        ),
        pytest.param(
            "{% if name == 'brutus' %}",
            None,
            "{% if name == 'brutus' %}",
            False,
            id="jinja-tag",
        ),
        # Complex inline Jinja
        pytest.param(
            "Some {{ text }} {% if website %} website value {% else %} other value {% endif %} is used",
            "Some {} {} website value {} other value {} is used",
            "SOME {{ text }} {% if website %} WEBSITE VALUE {% else %} OTHER VALUE {% endif %} IS USED",
            True,
            id="jinja-complex",
        ),
    ],
)
def test_translate(tmp_path, input, translated, output, fuzzy):
    os.chdir(tmp_path)
    pofile = tmp_path / "translations.po"
    write_po_file(pofile, [input])

    client = Mock()
    if translated:
        client.translate_text = Mock(return_value=mock_translation(translated))

    translate(client, pofile, "pt")

    if translated:
        client.translate_text.assert_called_once_with(translated, target_lang="pt-BR")
    else:
        client.translate_text.assert_not_called()

    # Confirm the translation has been integrated into original text
    po = polib.pofile(pofile)
    entry = po.find(input)
    assert entry.msgstr == output
    assert entry.fuzzy == fuzzy
