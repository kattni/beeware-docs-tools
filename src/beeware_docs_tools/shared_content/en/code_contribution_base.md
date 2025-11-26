# TODO: DELETE THIS WHEN CONTENT IS MOVED




### It's not just about writing tests!

Although we ensure that we test all of our code, the task isn't *just* about maintaining that level of testing. Part of the task is to audit the code as you go. You could write a comprehensive set of tests for a concrete life jacket... but a concrete life jacket would still be useless for the purpose it was intended!

As you develop tests, you should be checking that the core module is internally **consistent** as well. If you notice any method names that aren't internally consistent (e.g., something called `on_select` in one module, but called `on_selected` in another), or where the data isn't being handled consistently, flag it and bring it to our attention by raising a ticket. Or, if you're confident that you know what needs to be done, create a pull request that fixes the problem you've found.

### Waiting for feedback

Once you've written your code, test, and change note, you can submit your changes as a pull request. One of the core team will review your work, and give feedback. If any changes are requested, you can make those changes, and update your pull request; eventually, the pull request will be accepted and merged. Congratulations, you're a contributor to {{ formal_name }}!

## What next?

Rinse and repeat! If you've improved testing for one method, go back and do it again for *another* method! If you've implemented a new feature, implement *another* feature!

Most importantly - have fun!
