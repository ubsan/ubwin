from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding = 'utf-8') as f:
  long_description = f.read()

setup(
  name = 'ubwin',
  packages = [''],
  package_dir={'': 'src'},
  version = '0.1.0',
  description = 'NPM Windowing library',
  long_description = long_description,
  url = 'https://github.com/ubsan/ubwin',
  author = 'Nicole Mazzuca',
  author_email = 'npmazzuca@gmail.com',
  license = 'MIT',
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Windowing Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
  keywords = 'windowing tk window',
)
