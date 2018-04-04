Contributing to callable-pip
============================

This document is a set of guidelines, not a set of strict rules.
Feel free to propose changes to this document in a pull request.

Basic Rules
-----------

  - All of your code *must* pass ``flake8``. We won't consider merging code which
      doesn't pass ``flake8``
  - Check if there's a matching issue before opening a new issue or pull request
  - Any features which change the public API must include documentation updates

Reporting Bugs
--------------

The best bug reports are ones which follow the following rules:

  - *Use a clear descriptive title*
  - *Provide a specific example of how to reproduce*
  - *Explain what behavior you expected*
  - *Include a stacktrace* where applicable
  - Tell us, *which versions of python and pip are you running?*

Submitting Pull Requests
------------------------

  - *Make sure it merges cleanly*
  - *List any issues closed by the pull request*.
  - *Squash intermediate commits*
  - Code should pass ``pylint`` with a perfect ``10/10`` score (even the
    pedantic and silly rules)

A few basic ground rules for what ideal commits should look like:

  - No lines over 72 characters
  - No GitHub emoji -- use your words
  - Reference issues and pull requests where appropriate
  - Present tense and imperative mood
