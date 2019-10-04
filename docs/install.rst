.. _install:

Installation
============

Preliminary Git and GitHub setup
--------------------------------

First, some preliminary GitHub setup that will allow you to push and pull code securely:

* Create a `GitHub`_ account.
* `Generate an ssh keypair`_ (if you haven't already)
* `Add your ssh public key to GitHub`_


Install DataKit libraries
--------------------------

Next, install the core DataKit_ library and the datakit-project_ and datakit-github_ plugins:

.. code::

   pip install --user datakit-core datakit-project datakit-github


Generate GitHub API token
--------------------------

Next, you must generate a `personal GitHub API token`_ with all permissions for the **repo** scope.
This will enable datakit to automate interactions with the GitHub API (e.g. to auto-generate a project on GitHub).

Add API token to config
-----------------------

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



.. _DataKit: https://github.com/associatedpress/datakit-core
.. _datakit-github docs: https://datakit-github.readthedocs.io/en/latest/
.. _datakit-project: https://datakit-project.readthedocs.io/en/latest/
