# BeeWare Docs Tools Demo Section One { id="section-one" }

## Include External Markdown

The following section should have inline code and a code block. There should
be no text between the code block and the next header.

{%
    include-markdown "https://raw.githubusercontent.com/kattni/beeware-docs-tools/refs/heads/tooling/mkdocs/docs/include_content.md"
    start="<!--include-markdown-content-start-->"
    end="<!--include-markdown-content-end-->"
%}

## Footer Navigation

Navigate to *Section One - Page Two* for the final check.
