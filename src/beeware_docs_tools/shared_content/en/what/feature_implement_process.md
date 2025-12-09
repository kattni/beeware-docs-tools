Once the [proposal process](feature_proposal_process.md) has concluded, you should have a complete design for a new feature. That means it's time to start writing!

{% if not config.extra.macos_only %}

If your feature requires a platform-specific implementation, the proposal process should have validated that the idea *could* be implemented on all platforms. However, as the person implementing a new feature for the first time, you are not responsible for implementing the new feature for all platforms. You need to provide a complete implementation for *at least* one platform, including tests. For any other platforms, you will need to provide a "stub" implementation - an implementation that provides the bare interface definition, but raises a `NotImplementedError` or outputs a log message that the behavior isn't implemented on that platform.

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
