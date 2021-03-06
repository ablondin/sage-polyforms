## -*- encoding: utf-8 -*-
import os
import sys
from setuptools import setup
from codecs import open # To open the README file with proper encoding
from setuptools.command.test import test as TestCommand # for tests


# Get information from separate files (README, VERSION)
def readfile(filename):
    with open(filename,  encoding='utf-8') as f:
        return f.read()

# For the tests
class SageTest(TestCommand):
    def run_tests(self):
        errno = os.system("sage -t --force-lib sage_sample")
        if errno != 0:
            sys.exit(1)

setup(
    name = "polyforms",
    version = readfile("VERSION"), # the VERSION file is shared with the documentation
    description='A package for playing with polyforms',
    long_description = readfile("README.rst"), # get the long description from the README
    url='https://github.com/ablondin/sage-polyforms',
    author='Alexandre Blondin Massé',
    author_email='alexandre.blondin.masse@gmail.com', # choose a main contact email
    license='GPLv2+', # This should be consistent with the LICENCE file
    classifiers=[
      # How mature is this project? Common values are
      #   3 - Alpha
      #   4 - Beta
      #   5 - Production/Stable
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Science/Research',
      'Topic :: Combinatorics :: Polyforms',
      'Topic :: Computer Science :: Mathematics',
      'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
      'Programming Language :: Python :: 2.7',
    ], # classifiers list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords = "Polyform, polyomino, polycube, polyhex, polyiamond",
    packages = ['polyforms'],
    cmdclass = {'test': SageTest} # adding a special setup command for tests
)
