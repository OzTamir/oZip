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
    version = "1.1",
    author = "Oz Tamir",
    author_email = "TheOzTamir@gmail.com",
    description = ("A Simple Compression Solution"),
    license = "GNU GPL v2.0",
    keywords = "compression zip huffman",
    url = "http://oztamir.github.io/oZip/",
    packages=['oZip', 'oZip.core', 'oZip.core.Compression'],
    entry_points = {
            'console_scripts' : ['ozip = oZip.cli:run', 'ozip-gui = oZip.gui:main']
    },
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: System :: Archiving :: Compression",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
)