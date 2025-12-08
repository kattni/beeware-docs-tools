With the [proposal process](feature_proposal_process.md) concluded, if you have a complete design, it's time to start writing.

{% if not config.extra.macos_only %}

You are not responsible for implementing your feature for all platforms, however, the design process should validate that it will run on other platforms. Further, you will need to stub it out for all platforms. Essentially, there needs to exist an implementation for at least one platform, but that likely means there will need to be some kind of implementation for all other platforms, which can be as simple as `raise NotImplemented` or logging that the behavior doesn't work.

{% endif %}

### Contributing a new feature

{% macro content(template) %}{% include template %}{% endmacro %}
{% macro indented(template) %}{{ content(template)|indent }}{% endmacro %}

??? abstract "Set up a development environment"

    {{ indented("dev_environment.md") }}

??? abstract "Work from a branch"

    {{ indented("git_feature_branch.md") }}

??? abstract "Implement new functionality"

    {{ indented("code_run_test.md") }}

??? abstract "Write new documentation"

    {{ indented("docs_contribute.md") }}

??? abstract "Submit a pull request"

    {{ indented("pr_submit.md") }}

??? abstract "Add a change note"

    {{ indented("pr_change_note.md") }}
