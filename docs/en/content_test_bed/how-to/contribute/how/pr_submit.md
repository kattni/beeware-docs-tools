# Submitting a pull request

{% extends "how/pr_submit.md" %}

{% block end_matter %}

{% if config.extra.website %}

Your pull request may require further involvement from you after you've submitted it, such as adding a [change note](pr_change_note.md).

{% else %}

When submitting a pull request, you'll need to include a [change note](pr_change_note.md) before [the review](../next/pr_review.md) can begin.

{% endif %}

{% endblock %}
