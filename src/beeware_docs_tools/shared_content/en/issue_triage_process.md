The first step following an initial issue report is to triage the issue.

If a issue report has no comments from anyone other than the original reporter, the issue needs to be triaged. Triaging an issue involves taking the information provided by the reporter, and trying to reproduce it. If you can't reproduce the problem, report what you have found as a comment on the ticket, and pick another ticket.

Bug reports are often well-intentioned but incoherent or incomplete. If it comes to I tried to reproduce it, and couldn't. This is useful triage information.

Triage can be prompting the question to ask for more information about how the problem was actually happening in the first place.

## Contributing triaging an issue

{% macro content(template) %}{% include template %}{% endmacro %}
{% macro indented(template) %}{{ content(template)|indent }}{% endmacro %}

TODO: blurb.

??? abstract "Triage the issue"

    {{ indented("issue_reproduce.md") }}
