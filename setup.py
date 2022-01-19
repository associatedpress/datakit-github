#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
datakit-github
---------------

This plugin provides light-weight GitHub integration for the `DataKit command-line tool <https://datakit.ap.org>`_.

It's intended to streamline the process of generating a GitHub project and linking it to a local
directory containing a newly created project skeleton.

DataKit is a project by The Associated Press designed to streamline data analysis workflows.
To learn more about the wider DataKit ecosystem and how AP uses it, check out the
`official documentation for DataKit <https://datakit.ap.org>`_.

More information on the datakit-github plugin can be found below:

* Documentation: http://datakit-github.readthedocs.io/en/latest/
* GitHub: https://github.com/associatedpress/datakit-github
* PyPI: https://pypi.python.org/pypi/datakit-github
* Free and open source software: `ISC license  <https://github.com/associatedpress/datakit-github/blob/master/LICENSE>`_

"""

from setuptools import setup, find_packages

requirements = [
    'cliff',
    'datakit-core',
    'PyGithub',
]

test_requirements = [
    'flake8',
    'pytest',
    'vcrpy',
    'pytest-vcr'
]

setup(
    name='datakit-github',
    version='0.1.2',
    description="Light-weight GitHub integration for datakit workflows.",
    long_description=__doc__,
    long_description_content_type='text/x-rst',
    author="Serdar Tumgoren",
    author_email='zstumgoren@gmail.com',
    url='https://github.com/associatedpress/datakit-github',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'datakit.plugins': [
            'github integrate=datakit_github.commands:Integrate',
        ]
    },
    install_requires=requirements,
    license="ISC license",
    zip_safe=False,
    keywords='datakit',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    project_urls={
        "Documentation": "http://datakit-github.readthedocs.io/en/latest/",
        "Maintainer": "https://github.com/associatedpress",
        "Source": "https://github.com/associatedpress/datakit-github",
        "Tracker": "https://github.com/associatedpress/datakit-github/issues"
    },
)
