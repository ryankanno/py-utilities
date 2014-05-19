#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


setup(
    name='py-utilities',
    version='0.0.1',
    author='Ryan Kanno',
    author_email='ryankanno@localkinegrinds.com',
    url="https://github.com/ryankanno/py-utilities",
    packages=find_packages(),
    install_requires=['pytz', 'importlib', 'scrypt', 'xlrd', 'ordereddict'],
    license='MIT',
    tests_require=['flake8', 'mock', 'nose', 'nosexcover'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities'
    ],
)

# vim: filetype=python
