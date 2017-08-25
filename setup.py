from setuptools import setup, find_packages
from codecs import open
from os import path

abspath = path.abspath(path.dirname(__file__))

with open(path.join(abspath, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'testdatagen',
  py_modules = ['testdatagen'], 
  version = '0.1.12',
  description = 'Generates pipe delimited test data of names and addresses',
  long_description=long_description,
  author = 'Ramakrishna Nemani',
  author_email = 'ram.nemani@gmail.com',
  license='MIT',
  url = 'https://github.com/ramnemani/testdatagen', 
  download_url = 'https://github.com/ramnemani/testdatagen/archive/0.1.6.tar.gz',
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
