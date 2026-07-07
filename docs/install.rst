.. _install:

Installation
============

Preliminary Git and GitHub setup
--------------------------------

.. note::

   Existing users of git/GitHub should be able to skip a number of steps
   in this preliminary setup section.

First, some preliminary git/GitHub setup that will allow you to push and pull code securely:

* `Install git`_
* Configure git user and email

.. code::

   # NOTE: Substitute your own name and email below!!
   git config --global user.name "John Doe"
   git config --global user.email johndoe@example.com


* Create a `GitHub`_ account.
* `Generate an ssh keypair`_ (if you haven't already)
* `Add your ssh public key to GitHub`_


Install DataKit libraries
--------------------------

Next, install the core DataKit_ library together with the datakit-project_ and
datakit-github_ plugins. The recommended way is with uv_, which keeps the
``datakit`` command and its plugins in a single isolated environment:

.. code::

   uv tool install datakit-core --with datakit-project --with datakit-github

If you don't have uv, see its `installation docs
<https://docs.astral.sh/uv/getting-started/installation/>`_. See the DataKit_
docs for other ways to install and combine plugins.


Generate GitHub API token
--------------------------

Next, you must generate a `personal GitHub API token`_ with all permissions for the **repo** scope.
This will enable datakit to automate interactions with the GitHub API (e.g. to auto-generate a project on GitHub).

Add API token to config
-----------------------

With the API token in hand, store it using the generic ``datakit config`` command
family that ships with datakit-core_. Set the ``github_api_key`` value — because
it's a secret, you'll be prompted for it and your input stays hidden::

   $ datakit config set datakit-github github_api_key

Alternatively, fill in every unset value for the plugin interactively::

   $ datakit config init datakit-github

You can confirm the token is stored, and that it actually authenticates, with::

   $ datakit config list datakit-github
   $ datakit config verify datakit-github

.. note::

   ``datakit config`` writes ``~/.datakit/plugins/datakit-github/config.json``
   for you, so there's no need to create or hand-edit that file.


.. _GitHub: https://github.com
.. _`Generate an ssh keypair`: https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
.. _`Add your ssh public key to GitHub`: https://help.github.com/en/articles/adding-a-new-ssh-key-to-your-github-account
.. _`personal GitHub API token`: https://github.com/settings/tokens
.. _datakit-github: https://github.com/associatedpress/datakit-github
.. _`Install git`: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
.. _DataKit: https://github.com/associatedpress/datakit-core
.. _datakit-core: https://datakit-core.readthedocs.io/en/latest/
.. _uv: https://docs.astral.sh/uv/
.. _datakit-github docs: https://datakit-github.readthedocs.io/en/latest/
.. _datakit-project: https://datakit-project.readthedocs.io/en/latest/
