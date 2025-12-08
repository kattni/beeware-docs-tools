These are the steps to follow to write your documentation contribution to {{ formal_name }}.

Ensure you are able to [build the documentation](../how/docs_build.md) before beginning to write.

### Updating existing documentation

If you're editing the existing docs, you'll need to locate the file in the `/docs/en` directory. The file structure follows the page structure, so you can locate the file using the documentation URL.

### Adding new documentation

If you're adding a new document, there are a few more steps involved.

You'll need to create the document in the appropriate location within the `docs/en` directory.

Then, you'll need to update the `docs/en/SUMMARY.md` file to include your new file. `SUMMARY.md` is organized to reflect the `docs/en` directory structure, and directly determines the structure of the left sidebar. If you locate the directory containing your new document, and you see the following in `SUMMARY.md`, you do not need to change anything in the file:

```markdown
- ./path/to/file/*
```

You'll need to add an entry reflecting the location of your new document. Each entry is formatted as follows:

TODO: New document, adding to SUMMARY.md



Open the file in your editor, and find and update the text as required.

TODO: link to style guide etc.
