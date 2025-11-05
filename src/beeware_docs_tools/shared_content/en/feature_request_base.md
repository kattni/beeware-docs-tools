We're always open to suggestions and ideas for new features or documentation for {{ formal_name }}. The following details the process for submitting, and potentially implementing, your idea.

## Considerations for new features

Before you begin, keep the in mind that the BeeWare suite supports multiple platforms, and any new feature needs to fall into one of the following categories. It must:

* be suitable and implementable on all platforms (e.g. every platform has the concept of a button);
* be suitable for platforms of the same "type", and appropriate to ignore on other platforms (e.g. all mobile phones have accelerometers; not many desktops do, and therefore, it makes sense for an accelerometer API to exist for iOS and Android, but not for the desktop or web platforms);
* or, allow access to an internal platform feature without altering the public API (e.g. you can't add a clearly-Android-specific API, but you can open a door that makes it easier for end users to call an Android-specific API in code).

## Considerations for new documentation

When you have an idea for documentation, you'll want to determine what type of documentation fits your idea. As a starting point, you can ask yourself the following questions:

* Does it detail the process for completing a task? You're probably looking to submit a how-to guide.
* Does it provide information about a particular subject? You're probably looking to submit a topic guide.
* Is it an activity that amounts to a coherent learning path with an achievable goal? You may be looking to submit a tutorial.

Most of the time, your idea is likely to fit a how-to guide or a topic guide.

Other considerations include:

* Does it overlap with existing documentation? In which case, should it be an addition to an existing guide?
* How does it fit into the BeeWare ecosystem, i.e. which project's documentation would be the best fit for it?
* Is there a high-level concept that needs to be explained, or is it simply a gap where documenting a specific process is all that is required?
* Does the topic make sense for us to explain, or has someone else already covered it somewhere we can refer to it?

If you're unsure about any of this, don't worry! Submit your idea, and let us know in the initial discussion what you're unsure of, and we can help get it sorted.

## Submitting your idea

Once you've confirmed that your idea fits within the necessary considerations, you can begin the submission process.

### Research

The first step is to search {{ formal_name }}'s repository for existing [feature issues (labeled "enhancement")](https://github.com/beeware/{{ project_name }}/issues?q=is%3Aissue%20state%3Aopen%20label%3Aenhancement) or [documentation issues (labeled "documentation")](https://github.com/beeware/{{ project_name }}/issues?q=is%3Aissue%20state%3Aopen%20label%3Adocumentation), and [Discussions threads](https://github.com/beeware/{{ project_name }}/discussions) to see if the idea has been suggested before. If it has, and you have new context or ideas to add, include them in the existing thread. If you would like assistance with your research, you can optionally ask in the #dev channel on the [BeeWare Discord](https://beeware.org/bee/chat/). We may be able to point you in the direction of existing threads, or provide context of which you may not be aware.

### Propose

If you don't find any existing references to your idea, start a [Discussions threads](https://github.com/beeware/{{ project_name }}/discussions). Provide a high-level purpose and use case for your idea. Include any thoughts you have on what the feature would look like, if implemented, such as the general shape of an API, visual appearance, user interface, etc.

### Discuss

Next, the team will respond. This is your opportunity to participate in a conversation about your idea. We may ask for more details or context. The discussion will determine the next steps.

It's important to understand that not all ideas will be accepted. The reason this process starts with a proposal is to avoid you putting in all the work, only to find out there is a reason it can't be implemented. This doesn't mean it wasn't a good idea! There may be technical reasons it can't be implemented, such as, if it would be difficult or impossible to implement reliably, requires access to technology or software that isn't widely available, or if it may be difficult to maintain. As well, we may not accept it if it's sufficiently niche that it isn't a good fit for the project.

If we determine that your idea isn't a good fit, it doesn't necessarily mean you should give up on it. You can consider adding an entry point that allows you to implement your idea standalone. We are far more likely to implement a plugin interface or extension API that would allow your feature as a third-party plugin, than we are to implement a niche feature.

## Implementing your idea

If your idea is approved, you can begin the implementation process.

### Outline

Create a new [feature request issue](https://github.com/beeware/{{ project_name }}/issues/new/choose), in the {{ formal_name }} repository, that summarizes the discussion, linking to the discussion for context.

### Implement

Now it's time to implement your idea! [This guide][contribute-code] walks you through the steps necessary to contribute code to {{ formal_name }}.
