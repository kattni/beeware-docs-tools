# BeeWare Docs Tools

Tools for building BeeWare's documentation with a common theme and translations.

## Adding a new language

Weblate is able to generate a new language, however, adding a new language
also requires a few changes to the documentation repository.

Once a new language is generated, you'll need to add a new
`mkdocs.<language-code>.yml` file and update the `tox.ini` file.

The following example outlines how you would go about adding German to
this repo. The concepts are the same for any language in any of the docs
repos.

### The new MkDocs configuration file

The first thing to do is create a new file named `mkdocs.de.yml`, with the
following content:

```yaml
INHERIT: config.yml
site_name: BeeWare Docs Tools Demo
site_url: https://tutorial.beeware.org/de
docs_dir: de

theme:
  language: de

extra:
  translation_type: human
```

Here's what is going on in this file:

* This file inherits the configuration content from `config.yml`.
* The `site_name` value should be translated.
* The `site_url` value is the project site URL, followed by the language
  code.
* The `docs_dir` should be the language code.
* The `theme: language:` value should be the language code.
* The `extra: translation_type:` should be `human` or `machine`, depending
  on whether you provided the translation, or it was machine produced.

### The update to `tox.ini`

You'll need to make several changes to this file.

The final section of the `tox.ini` file is as follows:

```
[testenv:docs{,-lint,-translate,-all,-live,-en,-fr}]
# Docs are always built on Python 3.12. See also the RTD config.
base_python = py312
skip_install = true
deps =
    -r {tox_root}/requirements.docs.txt
commands:
    !lint-!all-!translate-!live-!en-!fr : build_md_translations --flat en
    translate : md2po --input docs{/}en --output {[docs]templates_dir} --pot --duplicates=merge
    translate : build_po_translations fr
    lint : markdown-checker --dir {[docs]docs_dir} --func check_broken_paths
    lint : markdown-checker --dir {[docs]docs_dir} --func check_broken_urls
    live : python -m mkdocs serve --clean --strict --config-file docs{/}mkdocs.en.yml --watch docs
    all : build_md_translations en fr
    en : build_md_translations --flat {posargs} en
    fr : build_md_translations --flat {posargs} fr
```

You'll need to add the following:

* The language code environment flag to the header line
* The language code exclusion to the first command, beginning with `!lint`
* The language code to the second `translate :` line
* The language code to the `all :` line
* A new line at the end that matches the other language-specific lines with the new language code.

The addition of German would result in the following:

```
[testenv:docs{,-lint,-translate,-all,-live,-en,-fr,-de}]
# Docs are always built on Python 3.12. See also the RTD config.
base_python = py312
skip_install = true
deps =
    -r {tox_root}/requirements.docs.txt
commands:
    !lint-!all-!translate-!live-!en-!fr-!de : build_md_translations --flat en
    translate : md2po --input docs{/}en --output {[docs]templates_dir} --pot --duplicates=merge
    translate : build_po_translations fr de
    lint : markdown-checker --dir {[docs]docs_dir} --func check_broken_paths
    lint : markdown-checker --dir {[docs]docs_dir} --func check_broken_urls
    live : python -m mkdocs serve --clean --strict --config-file docs{/}mkdocs.en.yml --watch docs
    all : build_md_translations en fr de
    en : build_md_translations --flat {posargs} en
    fr : build_md_translations --flat {posargs} fr
    de : build_md_translations --flat {posargs} de
```
