You can't fix a problem if you don't have the problem in the first place. Therefore, reproducing the issue is a prerequisite to fixing it. In software, problems are commonly referred to as ["bugs"](https://en.wikipedia.org/wiki/Software_bug), and issues are often called "bug reports".

Someone has provided a bug report. You need to validate that the steps the reporter describes are resulting in the bug being reported. Can you reproduce the same result by doing exactly what was described in the report? If you can't, you need to figure out why.

### Bugs in code

In an ideal situation, you have the same setup as the person who reported the bug, you follow the steps, and you're able to reproduce the bug. In many cases, though, it won't be so straightforward. Many bug reports include only vague explanations, and a vague set of conditions. The problem with that is, that bugs may vary based on the set of conditions involved, including how they're interacted with, various preconditions, operating system, operating system version, CPU architecture, or whether the user's machine is old and slow or new and fast. The more information we have about the situation surrounding the bug, the better. Try and reproduce the set of conditions that the reporter has provided. If you're unable to do so, your next step may need to be requesting more information from the person who reported the bug.

The best way to reproduce a bug is with the smallest possible example that still exhibits the issue. Most of the time reporters will not provide a minimum viable example, they will provide their large, complicated demo code. You'll want to reduce the report down to the simplest possible form that exhibits the issue; the best reproduction case is the smallest possible program. This reduction is itself helpful because it determines what the actual problem is. Essentially, anyone can take this example, run it, and it will result in the bug occurring.

### Bugs in documentation

Bugs in documentation can manifest in different ways. There are problems with formatting that result in rendering issues. Sometimes it's not even a bug; the person may have misread the documentation, or made a genuine mistake. This doesn't necessarily mean there isn't an issue with the documentation. The content may be unclear or imprecise, leaving room for confusion or misinterpretation. It's possible that a concept that should be discussed isn't, because it is completely undocumented.

When a bug is filed for a documentation issue, you'll want to verify that the issue reported actually still exists. In the case of rendering issues, you'll need to build the documentation to see if you can reproduce the issue. Content issues are a matter of reading to verify that no one has submitted an update.

### Update the issue

The final step in the triage process is to document your findings, by leaving a comment on the issue on GitHub. TODO: Russ - finish this.

{% block end_matter %}

{% endblock %}
