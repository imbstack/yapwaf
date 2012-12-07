#!/usr/bin/env python

from setuptools import setup

__version__ = '0.1'

setup(
  name = 'yapwaf',
  version = __version__,
  description = 'Simple WSGI application framework',
  author = 'Brian Stack',
  author_email = 'bis12@case.edu',
  url = 'http://github.com/bis12/yapwaf',
  packages = ['yapwaf'],
  provides = ['yapwaf'],
  scripts = ['scripts/yapwaf'],
  zip_safe = False,
  include_package_data=True,
  long_description=open("README").read(),
  install_requires = [
    'Jinja2',
    'SQLAlchemy',
    'Testify',
  ],
  classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Operating System :: OS Independent',
    'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
  ]
)
