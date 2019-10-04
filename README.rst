
.. image:: https://img.shields.io/pypi/v/datakit-github.svg
        :target: https://pypi.python.org/pypi/datakit-github

.. image:: https://img.shields.io/pypi/pyversions/datakit-github.svg
        :target: https://pypi.python.org/pypi/datakit-github

.. image:: https://img.shields.io/travis/associatedpress/datakit-github.svg
        :target: https://travis-ci.org/associatedpress/datakit-github

.. image:: https://readthedocs.org/projects/datakit-github/badge/?version=latest
        :target: https://datakit-github.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

=====================
DataKit GitHub plugin
=====================

Overview
========

This plugin provides light-weight GitHub integration for the DataKit_ command-line tool.
It's designed to streamline the process of generating a GitHub project
and linking it to a local directory containing a newly created project skeleton.
It's intended to be used in tandem with the datakit-project_ plugin, which
helps generate project skeletons for data work and software development.


* Documentation: http://datakit-github.readthedocs.io/en/latest/
* GitHub: https://github.com/associatedpress/datakit-github
* PyPI: https://pypi.python.org/pypi/datakit-github
* Free and open source software: `ISC license`_

.. _ISC license: https://github.com/associatedpress/datakit-github/blob/master/LICENSE

Features
========


The plugin provides the following features:

* Interactive selection of GitHub account for project creation
* Automated creation of a GitHub project
* Ability to set privacy level of repo
* Automated execution of git commands to bootstrap a project (init/add/commit)
* Linking of local Git repository to newly created GitHub project
* Automated "push" of initial commit to new GitHub project


In action
==========

Once datakit-github_ is installed, it becomes a cinch to "gitify" newly created
projects and integrate them with GitHub::

   # After generating an initial project structure...
   cd my-awesome-project

   # ...you can transform the project into a git repo
   # and integrate with GitHub with a single command
   datakit github integrate


.. note:: Check out the :ref:`install` and :ref:`usage` docs for more details.


.. _GitHub: https://github.com
.. _datakit-github: https://github.com/associatedpress/datakit-github
.. _DataKit: https://datakit.ap.org
.. _datakit-github docs: https://datakit-github.readthedocs.io/en/latest/
.. _datakit-project: https://datakit-project.readthedocs.io/en/latest/
