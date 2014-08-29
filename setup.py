import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "oZip",
    version = "1.0",
    author = "Oz Tamir",
    author_email = "TheOzTamir@gmail.com",
    description = ("A Simple Compression Solution"),
    license = "GNU GPL v2.0",
    keywords = "compression zip huffman",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['oZip'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
)