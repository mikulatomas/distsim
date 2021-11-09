#!/usr/bin/env python

"""The setup script."""

import pathlib
from setuptools import setup, find_packages

__author__ = 'Tomáš Mikula'
__email__ = 'mail@tomasmikula.cz'
__version__ = '0.2.1'
__license__ = 'MIT license'

setup(
    author=__author__,
    author_email=__email__,
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="Simulator of distributed system",
    license=__license__,
    long_description=pathlib.Path('README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='distributed system simulator simple education parallelism',
    name='distsim',
    packages=find_packages(include=['distsim', 'distsim.*']),
    extras_require={'docs': ['sphinx']},
    url='https://github.com/mikulatomas/distsim',
    version=__version__,
    zip_safe=False,
)
