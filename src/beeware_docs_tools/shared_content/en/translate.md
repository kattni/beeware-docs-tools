
if it is a language that we don't already have a translation for, we need to set up the translation in our content
What is the process for adding new translation:
    tox file, config file
once you've been added, it is at that point, log onto Weblate and start wroking through strings.
keep an eye on markup, ligth validation, but it can have issues
link text can update, link URLs shouldn't
trying to maintain tone more than word-for-word translation; try to be a bit friendly and colloqual in our English textx, try to maintain the spirit of that in your translations.
if the English is a particularly strong English idiom, don't feel beholden to maintain the idiom, and if it is a particularly slang or idiomatic term, don't be afriad to tell us we should change the English text, because even for English speakers, sometimes it's difficult to understand. Sometimes we need ot change the english text to make it easier for transaltor and readers.
Weblate processes everything on stringbystring basis, and batches changes up, every couple of hours, it will submit a bulk PR with all strings that have changed in that interfal. May take a couple of hours to show up on the webiste. essentially any translationo will be live in 4r hours. If not, likely cause, there is a markup error, and docs can't be built for language as a result, any markup problem in any string will block entire translation from being public. can keep an eye on taht by looking at RTD build page for your translation, for example the French translation is (URL HERE). That will show you the state of th emost recent build of that site., point to versions altest and stable. If unable to build, look at build log, and see if you can identify the source of the problem.

### Getting started with translating

To get started, you need let us know you're interested in translating so we can add you to the Weblate translation team. The first step is ensure you have an account on [Weblate](https://hosted.weblate.org). [Create a new account](https://hosted.weblate.org/accounts/register/) if you don't currently have one.

There are two options for letting us know that you'd like to help out with translations:

* If you're on Discord, join the [BeeWare server](https://beeware.org/bee/chat/), and head to the #translations channel.
* If you're not on Discord, you can create a new issue on the {{ formal_name }} repository.

In both cases, leave a message including the following information:

* Your Weblate username
* The language you are planning to which you are planning to translate content

Once we have this info, we'll get you added to the team.

### New translations

If the language you plan to help out with doesn't already exist, there is some setup necessary on our end before you can get started.

To set up a new language, the following steps must be completed:

* Create the `mkdocs.language-code.yml` file, with language-specific content.
* Update `tox.ini` to include the new language build commands.
* Update `config.yml` to include the language under `extra: alternate:`.

**The following demonstrates the necessary changes using German as an example.**

#### The new MkDocs configuration file

The first thing to do would be to create a new file named `mkdocs.de.yml` in the `docs` directory, with the following content:

```yaml
INHERIT: config.yml
site_name: BeeWare Demo zu Docs Tools
site_url: https://tutorial.beeware.org/de
docs_dir: de

theme:
  language: de

extra:
  translation_type: machine
```

Here's what is going on in this file:

* This file inherits the configuration content from `config.yml`.
* The `site_name` value is translated.
* The `site_url` value is the project site URL, followed by the language code.
* The `docs_dir` should be the language code.
* The `theme: language:` value should be the language code, as specified by the MkDocs Material theme. The list can be found [here](https://squidfunk.github.io/mkdocs-material/setup/changing-the-language/). For most languages, this will be the same as the `docs_dir` language code; but for some (in particular languages with locale variants like `zh_CN`), there are differences.
* The `extra: translation_type:` should be `machine` until the translation reaches 100% for the first time, at which point it should be `human`. It will revert to `machine` from `human` if it regresses to below 90%.

#### The update to `tox.ini`

You'll need to make several changes to the `tox.ini` file.

You would add the following:

* The new language code environment flag to the header line which begins `[testenv:docs`, with the language code preceded by a `-`, with no spaces included, e.g. `-de`.
* The new language code exclusion to the first command, which begins with `!lint`, preceded by `-!`, with no spaces included, e.g. `-!de`.
* The new language code to the end of the line beginning with `translate : build_po_translations`.
* The new language code to the end of the line beginning with `translate : update_machine_translations`
* A new command, beginning with, for example, `de : build_md_translations` for German, after the other existing language-specific commands that matches the content those commands with the new language code.
* The new language code to the end of the line beginning with `all,serve :`.

#### The update to `config.yml`

You need to add the language to `config.yml` for it to show up in the language selector in the header. Find the section beginning with `extra:`, and then locate the subsection beginning with `alternate:`. For German, you would add the following:

```yaml
    - name: Deutsch
      link: /de/
      lang: de
```

The language name should be translated into the language. The link must include the `/`s.

### Translation guidelines

The following items should _not_ be translated or updated:

* Commands. For example, in "You should run \`briefcase create\`.", only "You should run" should be translated.
* Namespaces; class, method, or attribute names.
* Reference links containing class, method or attribute names should be left as-is, including the backticks. The example link shown here would not be translated.

    ```markdown
    [`Class.attribute`][Class.attribute]
    ```

* Reference link link-content, as in `[Link text][link-content]`.
* Jinja directives. This is any content wrapped inside two pairs of matching curly braces, i.e. &lcub;&lcub; content &rcub;&rcub;, or a matching pair of single curly braces followed by a percent sign, i.e. &lcub;% content %&rcub;. Note: See the [Macros documentation](https://mkdocs-macros-plugin.readthedocs.io/en/latest/pages/) for further details.
* Custom anchors. They are found after headers or above some content, and are formatted as `{ #anchor }`.
* Admonition _syntax_. As shown here, the word "admonition" should not be translated. This goes for all styles of admonitions, including notes, warnings, etc. See the next section for information on translating the rest of the content.

    ```markdown
    /// admonition | Title

    Content.

    ///
    ```

* Backticks are meant to stay as backticks; they are used for formatting both inline code and code blocks.
* The syntax for including external content. This is anything on the same line as `-8<-`, or on the lines between two `-8<-` on separate lines.

The following items _should_ be translated:

* Reference link text, as in `[Link text][link-content]`.
* The admonition titles and content. As shown below, "Title" and "Content." should be translated. See above for information on the syntax.

    ```markdown
    /// admonition | Title

    Content.

    ///
    ```
