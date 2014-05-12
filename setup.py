#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


setup(name='py-utilities',
      version='0.0.1',
      description='A set of Python utilities',
      author='Ryan Kanno',
      author_email='ryankanno@localkinegrinds.com',
      packages=find_packages(),
      url="https://github.com/ryankanno/py-utilities",
      install_requires=['pytz', 'importlib', 'scrypt'],
      license='MIT',
      tests_require=['flake8', 'mock', 'nose', 'nosexcover'])

# vim: filetype=python
