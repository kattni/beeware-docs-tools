Before you submit a pull request, there's a few bits of housekeeping to do.

### Submit from a feature branch, not your `main` branch

Before you start working on your change, make sure you've created a branch. By default, when you clone your repository fork, you'll be checked out on your `main` branch. This is a direct copy of {{ formal_name }}'s `main` branch.

While you *can* submit a pull request from your `main` branch, it's preferable if you *don't* do this. If you submit a pull request that is *almost* right, the core team member who reviews your pull request may be able to make the necessary changes, rather than giving feedback asking for a minor change. However, if you submit your pull request from your `main` branch, reviewers are prevented from making modifications.

Instead, you should make your changes on a *feature branch*. A feature branch has a simple name to identify the change that you've made. For example, if you've found a bug that causes a display problem on Windows 11, you might create a feature branch `fix-win11-display`. If your bug relates to a specific issue that has been reported, it's also common to reference that issue number in the branch name (e.g., `fix-1234`).

To create a `fix-win11-display` feature branch, run:

{% if not config.extra.macos_only %}

/// tab | macOS

{% endif %}

```console
(.venv) $ git switch -c fix-win11-display
```

{% if not config.extra.macos_only %}

///

/// tab | Linux

```console
(.venv) $ git switch -c fix-win11-display
```

///

/// tab | Windows

```doscon
(.venv) C:\...>git switch -c fix-win11-display
```

///

{% endif %}

Commit your changes to this branch, then push to GitHub and create a pull request.

### Working with pre-commit

When you commit any change, pre-commit will run automatically. If there are any issues found with the commit, this will cause your commit to fail. Where possible, pre-commit will make the changes needed to correct the problems it has found:

{% if not config.extra.macos_only %}

/// tab | macOS

{% endif %}

```console
(.venv) $ git add some/interesting_file.py
(.venv) $ git commit -m "Minor change"
check toml...............................................................Passed
check yaml...............................................................Passed
check for case conflicts.................................................Passed
check docstring is first.................................................Passed
fix end of files.........................................................Passed
trim trailing whitespace.................................................Passed
ruff format..............................................................Failed
- hook id: ruff-format
- files were modified by this hook

1 file reformatted, 488 files left unchanged

ruff check...............................................................Passed
codespell................................................................Passed
```

{% if not config.extra.macos_only %}

///

/// tab | Linux

```console
(.venv) $ git add some/interesting_file.py
(.venv) $ git commit -m "Minor change"
check toml...............................................................Passed
check yaml...............................................................Passed
check for case conflicts.................................................Passed
check docstring is first.................................................Passed
fix end of files.........................................................Passed
trim trailing whitespace.................................................Passed
ruff format..............................................................Failed
- hook id: ruff-format
- files were modified by this hook

1 file reformatted, 488 files left unchanged

ruff check...............................................................Passed
codespell................................................................Passed
```

///

/// tab | Windows

```doscon
(.venv) C:\...>git add some/interesting_file.py
(.venv) C:\...>git commit -m "Minor change"
check toml...............................................................Passed
check yaml...............................................................Passed
check for case conflicts.................................................Passed
check docstring is first.................................................Passed
fix end of files.........................................................Passed
trim trailing whitespace.................................................Passed
ruff format..............................................................Failed
- hook id: ruff-format
- files were modified by this hook

1 file reformatted, 488 files left unchanged

ruff check...............................................................Passed
codespell................................................................Passed
```

///

{% endif %}

You can then re-add any files that were modified as a result of the pre-commit checks, and re-commit the change.

{% if not config.extra.macos_only %}

/// tab | macOS

{% endif %}

```console
(.venv) $ git add some/interesting_file.py
(.venv) $ git commit -m "Minor change"
check toml...............................................................Passed
check yaml...............................................................Passed
check for case conflicts.................................................Passed
check docstring is first.................................................Passed
fix end of files.........................................................Passed
trim trailing whitespace.................................................Passed
ruff format..............................................................Passed
ruff check...............................................................Passed
codespell................................................................Passed
[bugfix e3e0f73] Minor change
1 file changed, 4 insertions(+), 2 deletions(-)
```

{% if not config.extra.macos_only %}

///

/// tab | Linux

```console
(.venv) $ git add some/interesting_file.py
(.venv) $ git commit -m "Minor change"
check toml...............................................................Passed
check yaml...............................................................Passed
check for case conflicts.................................................Passed
check docstring is first.................................................Passed
fix end of files.........................................................Passed
trim trailing whitespace.................................................Passed
ruff format..............................................................Passed
ruff check...............................................................Passed
codespell................................................................Passed
[bugfix e3e0f73] Minor change
1 file changed, 4 insertions(+), 2 deletions(-)
```

///

/// tab | Windows

```doscon
(.venv) C:\...>git add some\interesting_file.py
(.venv) C:\...>git commit -m "Minor change"
check toml...............................................................Passed
check yaml...............................................................Passed
check for case conflicts.................................................Passed
check docstring is first.................................................Passed
fix end of files.........................................................Passed
trim trailing whitespace.................................................Passed
ruff format..............................................................Passed
ruff check...............................................................Passed
codespell................................................................Passed
```

///

{% endif %}

Once everything passes, you're ready for the next steps.

### Add change information for release notes

When you submit this change as a pull request, you need to add a *change note*. {{ formal_name }} uses [`towncrier`](https://pypi.org/project/towncrier/) to automate building the release notes for each release. Every pull request must include at least one file in the `changes/` directory that provides a short description of the change implemented by the pull request.

The change note should be in Markdown format, in a file that has name of the format `<id>.<fragment type>.md`. If the change you are proposing will fix a bug or implement a feature for which there is an existing issue number, the ID will be the number of that ticket. If the change has no corresponding issue, the PR number can be used as the ID. You won't know this PR number until you push the pull request, so the first CI pass will fail the `towncrier` check; add the change note and push a PR update and CI should then pass.

There are five allowed fragment types:

- `feature`: The PR adds a new behavior or capability that wasn't previously possible (e.g., adding support for a new packaging format, or a new feature in an existing packaging format);
- `bugfix`: The PR fixes a bug in the existing implementation;
- `doc`: The PR is an significant improvement to documentation;
- `removal`; The PR represents a backwards incompatible change in the {{ formal_name }} API; or
- `misc`; A minor or administrative change (e.g., fixing a typo, a minor language clarification, or updating a dependency version) that doesn't need to be announced in the release notes.

This description in the change note should be a high level summary of the change from the perspective of the user, not a deep technical description or implementation detail. It is distinct from a commit message - a commit message describes what has been done so that future developers can follow the reasoning for a change; the change note is a "user facing" description. For example, if you fix a bug related to project naming, the commit message might read:

> Disallow project names that begin with a number.

The corresponding change note would read something like:

> Project names can no longer begin with a number.

Some PRs will introduce multiple features and fix multiple bugs, or introduce multiple backwards incompatible changes. In that case, the PR may have multiple change note files. If you need to associate two fragment types with the same ID, you can append a numerical suffix. For example, if PR 789 added a feature described by ticket 123, closed a bug described by ticket 234, and also made two backwards incompatible changes, you might have 4 change note files:

- `123.feature.md`
- `234.bugfix.md`
- `789.removal.1.md`
- `789.removal.2.md`

For more information about `towncrier` and fragment types see [News Fragments](https://towncrier.readthedocs.io/en/stable/tutorial.html#creating-news-fragments). You can also see existing examples of news fragments in the `changes` directory of the {{ formal_name }} repository. If this folder is empty, it's likely because {{ formal_name }} has recently published a new release; change note files are deleted and combined to update the [release notes]() with each release. You can look at that file to see the style of comment that is required; you can look at [recently merged PRs](https://github.com/beeware/briefcase/pulls?q=is%3Apr+is%3Amerged) to see how to format your change notes.
