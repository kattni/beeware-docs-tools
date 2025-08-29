# Shared content test bed

This section is included for the purposes of verifying the shared content provided from this repo for use in the rest of the BeeWare documentation. "Shared content" refers to documents or sections of documents that are common to multiple other repos. They are stored here for inclusion across those repos. This means there is a single source when updates are required, and that change will populate across all repos using that shared content.

If you are updating existing content, the following steps are not necessary. You can simply build the test site, and see your updates rendered.

If you are creating a new shared documentation file, complete the following:

1. Create the new file in the `shared_content` directory.
      * For the style guide, you would create `style_guide.md`.
2. Update the `Shared content test bed` section in `/docs/SUMMARY.md` to include the new file and path, at the same indentation level as the other items in that section.
      * For `style_guide.md`, you would add `- [Style guide](shared_content/style_guide.md)`.

Once these steps are completed, you can build the test site and view your new documentation rendered.
