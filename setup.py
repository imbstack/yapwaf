#!/usr/bin/env python

from setuptools import setup, find_packages
import yapwaf

setup(
  name = 'yapwaf',
  version = yapwaf.__version__,
  description = 'Simple lightweight WSGI application framework',
  author = 'Brian Stack',
  author_email = 'bis12@case.edu',
  url = 'http://github.com/bis12/yapwaf',
  download_url = \
    'http://github.com/bis12/yapwaf/tarball/yapwaf-%s' % yapwaf.__version__,
  packages = find_packages('yapwaf', exclude=['ez_setup']),
  provides = ['yapwaf'],
  long_description=open("README.rst").read(),
  install_requires=open('requirements.txt', 'r').readlines(),
  classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Operating System :: OS Independent',
    'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
  ]
)
