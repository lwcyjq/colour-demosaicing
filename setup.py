#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pypi Setup
==========
"""

from __future__ import unicode_literals

import os
import re
import sys
from setuptools import setup
from setuptools import find_packages

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2015-2019 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = [
    'SHORT_DESCRIPTION', 'LONG_DESCRIPTION', 'INSTALLATION_REQUIREMENTS',
    'DOCS_REQUIREMENTS', 'TESTS_REQUIREMENTS', 'DEVELOPMENT_REQUIREMENTS'
]

SHORT_DESCRIPTION = 'Colour - Demosaicing'

LONG_DESCRIPTION = open('README.rst').read()

INSTALLATION_REQUIREMENTS = ['colour-science>=0.3.11']

if os.environ.get('READTHEDOCS') == 'True':
    INSTALLATION_REQUIREMENTS = [
        'colour-science>=0.3.8', 'mock==1.0.1', 'sphinxcontrib-bibtex'
    ]

DOCS_REQUIREMENTS = [
    'sphinx>=1.6.6', 'sphinxcontrib-bibtex', 'sphinx_rtd_theme'
]

TESTS_REQUIREMENTS = ['coverage>=3.7.1', 'flake8>=2.1.0', 'nose>=1.3.4']

DEVELOPMENT_REQUIREMENTS = DOCS_REQUIREMENTS + TESTS_REQUIREMENTS + [
    'invoke', 'restructuredtext_lint', 'twine', 'yapf=0.23.0'
]
if sys.version_info[:2] >= (3, 2):
    DEVELOPMENT_REQUIREMENTS += [
        'biblib @ git+ssh://git@github.comcolour-science/biblib'
        '@v0.1.0#egg=biblib'
    ]


def get_version():
    """
    Returns the package full version.

    Returns
    -------
    unicode
        Package full version.
    """

    with open(os.path.join('colour_demosaicing',
                           '__init__.py')) as file_handle:
        file_content = file_handle.read()
        major_version = re.search("__major_version__\s+=\s+'(.*)'",
                                  file_content).group(1)
        minor_version = re.search("__minor_version__\s+=\s+'(.*)'",
                                  file_content).group(1)
        change_version = re.search("__change_version__\s+=\s+'(.*)'",
                                   file_content).group(1)

        return '.'.join((major_version, minor_version, change_version))


setup(
    name='colour-demosaicing',
    version=get_version(),
    author=__author__,
    author_email=__email__,
    include_package_data=True,
    packages=find_packages(),
    scripts=[],
    url='http://github.com/colour-science/colour-demosaicing',
    license=__license__,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    install_requires=INSTALLATION_REQUIREMENTS,
    extras_require={
        'docs': DOCS_REQUIREMENTS,
        'development': DEVELOPMENT_REQUIREMENTS,
        'tests': TESTS_REQUIREMENTS
    },
    classifiers=[
        'Development Status :: 3 - Alpha', 'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research', 'License :: OSI Approved',
        'Natural Language :: English', 'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering', 'Topic :: Software Development'
    ])
