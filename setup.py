#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

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
    version='0.1.0',
    description="Light-weight GitHub integration for datakit workflows.",
    long_description=readme + '\n\n' + history,
    author="Serdar Tumgoren",
    author_email='zstumgoren@gmail.com',
    url='https://github.com/associatedpress/datakit-github',
    packages=[
        'datakit_github',
    ],
    package_dir={'datakit_github':
                 'datakit_github'},
    include_package_data=True,
    entry_points={
        'datakit.plugins': [
            'github integrate=datakit_github.commands:Integrate',
        ]
    },
    install_requires=requirements,
    license="ISC license",
    zip_safe=False,
    keywords='datakit-github',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
