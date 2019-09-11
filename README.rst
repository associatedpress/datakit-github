
.. image:: https://img.shields.io/pypi/v/datakit-github.svg
        :target: https://pypi.python.org/pypi/datakit-github

.. image:: https://img.shields.io/pypi/pyversions/datakit-github.svg
        :target: https://pypi.python.org/pypi/datakit-github

.. image:: https://img.shields.io/travis/associatedpress/datakit-github.svg
        :target: https://travis-ci.org/associatedpress/datakit-github

.. image:: https://readthedocs.org/projects/datakit-github/badge/?version=latest
        :target: https://datakit-github.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

===============================
DataKit GitHub plugin
===============================

Commands to manage project integration with GitHub.

Overview
========

Light-weight GitHub integration for DataKit workflows.

* Documentation: http://datakit-github.readthedocs.io/en/latest/
* GitHub: https://github.com/associatedpress/datakit-github
* PyPI: https://pypi.python.org/pypi/datakit-github
* Free and open source software: `ISC license`_

.. _ISC license: https://github.com/associatedpress/datakit-github/blob/master/LICENSE

Features
========

This plugin is designed to streamline the process of generating a GitHub project
and linking it to a local directory containing a newly created project skeleton.
It's intended to be used in tandem with the datakit-project_ plugin, which
helps generate project skeletons for data work and software development.

The plugin provides the following features:

* Interactive selection of GitHub account for project creation
* Automated creation of a GitHub project
* Ability to set privacy level of repo
* Automated execution of git commands to bootstrap a project (init/add/commit)
* Linking of local Git repository to newly created GitHub project
* Automated "push" of initial commit to new GitHub project

Install/set-up
==============

First, some preliminary GitHub setup that will allow you to push and pull code securely:

* Create a `GitHub`_ account.
* `Generate an ssh keypair`_ (if you haven't already)
* `Add your ssh public key to GitHub`_

Next, install the core datakit_ library and the datakit-project_ and datakit-github_ plugins:

.. code::

   pip install --user datakit-core datakit-project datakit-github


Next, you must generate a `personal GitHub API token`_ with all permissions for the **repo** scope.
This will enable datakit to automate interactions with the GitHub API (e.g. to auto-generate a project on GitHub).

With the API token in hand, store it in the configuration file for the *datakit-github* plugin.
This file must be located inside the home directory for datakit configurations.

On Mac/Linux systems, you should create `~/.datakit/plugins/datakit-github/config.json` file with
the below commands::

  # First ensure the plugin directory exists
  mkdir -p ~/.datakit/plugins/datakit-github/
  # Create a blank configuration file
  touch ~/.datakit/plugins/datakit-github/config.json

Lastly, edit the newly created file so that it contains the below, replacing
`GITHUB_API_TOKEN` with your actual key::

   {"github_api_key": "GITHUB_API_TOKEN"}

.. note::

   Please be sure to avoid extraneous white space and preserve the double quotes. This must be valid JSON!!


.. _GitHub: https://github.com
.. _`Generate an ssh keypair`: https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
.. _`Add your ssh public key to GitHub`: https://help.github.com/en/articles/adding-a-new-ssh-key-to-your-github-account
.. _`personal GitHub API token`: https://github.com/settings/tokens
.. _datakit-github: https://github.com/associatedpress/datakit-github


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


.. _datakit: https://github.com/associatedpress/datakit-core
.. _datakit-github docs: https://datakit-github.readthedocs.io/en/latest/
.. _datakit-project: https://datakit-project.readthedocs.io/en/latest/
