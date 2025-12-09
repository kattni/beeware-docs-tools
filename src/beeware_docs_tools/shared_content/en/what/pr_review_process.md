We're always happy to have reviews from contributors, regardless of their experience level.

### Why review contributions?

Every contribution that is submitted needs to be reviewed, regardless of whether it was submitted by a core team member, a first-time contributor, or anyone anywhere between. Everyone has the potential to miss something, from making a simple typo to introducing a major bug. The review process is in place to provide an extra safety net.

The purpose of the review process is to ensure all content, including code and documentation, is as bug-free and easy-to-maintain as possible. Anything you can do to further that goal is a welcome contribution. This can be anything, ranging from spotting obvious typos, to finding edge cases in the API usage that aren't being caught, to noting a testing regimen could be more robust, or other ways of structuring the changes or architecture that may make it easier to maintain or extend.

### Can I review?

Yes! You can offer a review on any pull request you see open on {{ formal_name }}.

As a first-time contributor, you should feel free to review any pull request you find, even if it was submitted by a core team member. Keep in mind, though, being new to the project, you may be missing context. That doesn't necessarily mean it's your problem; there may be something in the contribution that needs to be more clearly explained or documented.

### Contributing a pull request review

{% macro content(template) %}{% include template %}{% endmacro %}
{% macro indented(template) %}{{ content(template)|indent }}{% endmacro %}

??? abstract "Providing a pull request review"

    {{ indented("how/pr_review_provide.md") }}
