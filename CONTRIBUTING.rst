.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/associatedpress/datakit-github/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
and "help wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

datakit-github could always use more documentation, whether as part of the
official datakit-github docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/associatedpress/datakit-github/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `datakit-github` for local development.

datakit-github uses uv_ to manage its virtual environment and dependencies.
Install uv first if you don't have it (see its `installation docs
<https://docs.astral.sh/uv/getting-started/installation/>`_).

1. Fork the `datakit-github` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/datakit-github.git
    $ cd datakit-github/

3. Create the virtual environment and install all dependencies (including the
   dev tools) from ``uv.lock``, then activate it::

    $ uv sync
    $ source .venv/bin/activate

   uv picks a supported interpreter automatically; datakit-github supports
   Python 3.10 through 3.13.

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass the linter and
   the tests. The Makefile wraps the common tasks::

    $ make lint       # uv run ruff check datakit_github tests
    $ make test       # uv run pytest
    $ make test-all   # uv run tox across Python 3.10-3.13

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should pass ``make test-all`` across the supported Python
   versions (3.10 through 3.13).

.. _uv: https://docs.astral.sh/uv/
