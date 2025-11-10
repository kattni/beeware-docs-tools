TODO: Intro paragraph

## What can I do to contribute?

There are many paths to contributing to BeeWare. You can choose the option that works best for you based on your interests and skill level.

Depending on your level of expertise, or areas of interest, there are a number of ways you can contribute to {{ formal_name }}.

{% block contribution_topics %}

{% block contribution_topics_bug_fix %}

### Fix a bug

{{ formal_name }}'s issue tracker logs the list of [known issues](https://github.com/beeware/{{ project_name }}/issues?q=is%3Aopen+is%3Aissue+label%3Abug). Any of these issues are candidates to be worked on. This list can be filtered by platform, so you can focus on issues that affect the platforms you're able to test on. There's also a filter for [good first issues](https://github.com/beeware/{{ project_name }}/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) . These have been identified as problems that have a known cause, and we believe the fix *should* be relatively straightforward (although we might be wrong in our analysis).

We don't have any formal process of "claiming" or "assigning" issues; if you're interested in a ticket, leave a comment that says you're working on it. If there's an existing comment that says someone is working on the issue, and that comment is recent, then leave a comment asking if they're still working on the issue. If you don't get a response in a day or two, you can assume the issue is available. If the most recent comment is more than a few weeks old, it's probably safe to assume that the issue is still available to be worked on.

If an issue is particularly old (more than 6 months), it's entirely possible that the issue has been resolved, so the first step is to verify that you can reproduce the problem. Use the information provided in the bug report to try and reproduce the problem. If you can't reproduce the problem, report what you have found as a comment on the ticket, and pick another ticket.

If a bug report has no comments from anyone other than the original reporter, the issue needs to be triaged. Triaging a bug involves taking the information provided by the reporter, and trying to reproduce it. Again, if you can't reproduce the problem, report what you have found as a comment on the ticket, and pick another ticket.

If you can reproduce the problem - try to fix it! Work out what combination of code is implementing the feature, and see if you can work out what isn't working correctly.

If you're able to fix the problem, you'll need to [add tests][run-test-suite] to verify that the problem has been fixed (and to prevent the issue from occurring again in future).

Even if you can't fix the problem, reporting anything you discover as a comment on the ticket is worthwhile. If you can find the source of the problem, but not the fix, that knowledge will often be enough for someone who knows more about a platform to solve the problem. Even a good reproduction case (a sample app that does nothing but reproduce the problem) can be a huge help.

{% endblock %}

{% block contribution_topics_docs %}

### Contribute improvements to documentation

We've got a [separate contribution guide][contribute-docs] for documentation contributions. It covers how to set up your development environment to build {{ formal_name }}'s documentation, and separate ideas for what to work on.

{% endblock %}

{% block contribution_topics_new_feature %}

### Add a new feature

Can you think of a feature that {{ formal_name }} should have? Propose a new API or feature, and provide a sample implementation. If you don't have any ideas of your own, the {{ formal_name }} issue tracker has some [existing feature suggestions](https://github.com/beeware/{{ project_name }}/issues?q=is%3Aopen+is%3Aissue+label%3Aenhancement) that you could try to implement.

Again, you'll need to add unit tests for any new features you add.

{% endblock %}

{% endblock %}
