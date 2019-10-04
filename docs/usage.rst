.. _usage:

Usage
=====

Create a new project using the datakit-project_ plugin.  For example,
you could try AP's template for R-based projects::

    datakit project create -t https://github.com/associatedpress/cookiecutter-r-project.git

The above command will prompt you for various bits of information, including a project name.
Let's assume we chose `awesome-proj` as the name.

To integrate the project with GitHub, navigate into the newly created
project directory and execute the following command::

   cd awesome-proj
   datakit github integrate

The above should trigger a series of prompts that allow you to select the GitHub account where the
new repo should be created, and whether to make the repo private or public.

The command will auto-generate the GitHub project, link your local code to the new project, and
push the newly generated project skeleton to GitHub as your first commit.

.. note:: The command will warn you if a project name already exists on the GitHub account.
   In such a case, you must either choose a different account (e.g. if
   you're a member of another GitHub organization), rename the project, or remove the previously
   existing project from GitHub.


.. _datakit-github docs: https://datakit-github.readthedocs.io/en/latest/
.. _datakit-project: https://datakit-project.readthedocs.io/en/latest/
