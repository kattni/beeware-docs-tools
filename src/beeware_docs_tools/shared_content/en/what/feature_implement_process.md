With the proposal process concluded, if you have a complete design, it's time to start writing.

{% if not config.extra.macos_only %}

You are not responsible for implementing your feature for all platforms, however, the design process should validate that it will run on other platforms. Further, you will need to stub it out for all platforms. Essentially, there needs to exist an implementation for at least one platform, but that likely means there will need to be some kind of implementation for all other platforms, which can be as simple as `raise NotImplemented` or logging that the behavior doesn't work.

{% endif %}

### Contributing new functionality

{% macro content(template) %}{% include template %}{% endmacro %}
{% macro indented(template) %}{{ content(template)|indent }}{% endmacro %}

??? abstract "Set up a development environment"

    {{ indented("how/dev_environment.md") }}

??? abstract "Work from a branch"

    {{ indented("how/git_feature_branch.md") }}

??? abstract "Avoid scope creep"

    {{ indented("how/scope_creep.md") }}

??? abstract "Implement a new code feature"

    {{ indented("how/code_run_test.md") }}

??? abstract "Submit a pull request"

    {{ indented("how/pr_submit.md") }}

??? abstract "Add a change note"

    {{ indented("how/pr_change_note.md") }}
