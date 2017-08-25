# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'testdatagen',
  packages = ['testdatagen'], 
  version = '0.1.16',
  description = 'Generates pipe delimited test data of names and addresses',
  long_description=long_description,
  author = 'Ramakrishna Nemani',
  author_email = 'ram.nemani@gmail.com',
  license='MIT',
  url = 'https://github.com/ramnemani/testdatagen', 
  download_url = 'https://github.com/ramnemani/testdatagen/archive/0.1.16.tar.gz',
  package_data={'testdatagen': ['data/*.csv']},
  keywords = ['testdata', 'test data', 'fake'], 
  classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Topic :: Utilities'
        ]
)
