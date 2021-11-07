#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

__author__ = 'Tomáš Mikula'
__email__ = 'mail@tomasmikula.cz'
__version__ = '0.2.0'
__license__ = 'MIT license'

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

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
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='distsim',
    name='distsim',
    packages=find_packages(include=['distsim', 'distsim.*']),
    setup_requires=setup_requirements,
    extras_require={'docs': ['sphinx']},
    url='https://github.com/mikulatomas/distsim',
    version=__version__,
    zip_safe=False,
)
