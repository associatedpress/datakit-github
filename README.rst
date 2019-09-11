
.. image:: https://img.shields.io/pypi/v/datakit-github.svg
        :target: https://pypi.python.org/pypi/datakit-github

.. image:: https://img.shields.io/pypi/pyversions/datakit-github.svg
        :target: https://pypi.python.org/pypi/datakit-github

.. image:: https://img.shields.io/travis/associatedpress/datakit-github.svg
        :target: https://travis-ci.org/associatedpress/datakit-github

.. image:: https://readthedocs.org/projects/datakit-github/badge/?version=latest
        :target: https://datakit-github.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Overview
========

Light-weight GitHub integration for datakit workflows.

* Documentation: http://datakit-github.readthedocs.io/en/latest/
* Github: https://github.com/associatedpress/datakit-github
* PyPI: https://pypi.python.org/pypi/datakit-github
* Free and open source software: `ISC license`_

.. _ISC license: https://github.com/associatedpress/datakit-github/blob/master/LICENSE

Features
========

* Runs initial git commands to bootstrap a project (init/add/commit)
* Creates GitHub project
* Links local repo to newly created GitHub project
* Pushes first commit to new GitHub project

Quickstart
==========

To use this datakit_ plugin::

  $ pip install datakit-github

Check out the available commands::

  $ datakit --help

.. note:: See the `datakit-github docs`_ for more detailed usage info.


.. _datakit: https://github.com/associatedpress/datakit-core
.. _datakit-github docs: https://datakit-github.readthedocs.io/en/latest/
