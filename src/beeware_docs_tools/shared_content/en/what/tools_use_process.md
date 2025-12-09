One of the most valuable pieces of feedback we can get is from people trying to use the BeeWare tools, and discovering there is a point of friction or a missing feature. It's incredibly useful to us to understand any difficulties you might experience when using the tools for real-world purposes.

Think of the thing you've always wanted to build, and try building it. If it turns out you are able to build your project, congratulations! You have the thing you always wanted. However, if you're not successful, letting us know why is extremely helpful. Was there a missing feature? Is the documentation confusing or lacking in some aspect? You sharing having faced a complexity we haven't considered helps us improve the experience for everyone.

If you do experience any problems, start a discussion, as it may be the start of a new issue or feature proposal.

### Contributing tool usage

{% macro content(template) %}{% include template %}{% endmacro %}
{% macro indented(template) %}{{ content(template)|indent }}{% endmacro %}

??? abstract "Submit a new issue"

    {{ indented("how/issue_submit.md") }}

??? abstract "Propose a new feature"

    {{ indented("how/feature_proposal.md") }}
