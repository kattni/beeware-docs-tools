# BeeWare Docs Tools Demo Section One

## Include External Markdown from a Local File

The following section should have only a header, and a paragraph with inline code
followed by a code block. There should be no text between the code block and the
next header. This verifies that the external include extension is working with
local files.

-8<- "include_content.md:local-content"

## Include External Markdown from a URL

The following section should have only a header, some text and a Markdown list.
This verifies that the external include extension is working, and that
`url_download` is enabled.

-8<- "https://raw.githubusercontent.com/beeware/beeware-docs-tools/refs/heads/main/docs/include_content.md:remote-content"

## Footer Navigation

Navigate to *Section One - Page Two* for the final check.
