oZip - Simple compression solution in Python
============================================

Installation
------------

To install oZip, simply use pip:

::

    $ pip install ozip

If for some reason pip is unavailable (Or you’re on Windows), you can
install by running the following commands:

::

    $ git clone https://github.com/OzTamir/oZip
    $ cd oZip
    $ python setup.py install

If you have any problem with the setup process, you are welcomed to open
a Issue in the project’s repository.

Usage
-----

To compress a file run the following command:

::

    $ ozip -i <Path to file>

This will create a file.ext.ozip in the same path.

To decompress a file, run the following command:

::

    $ ozip -i <oZip File> -d

This will decompress the file in the same path.

Roadmap
-------

Going forward there are still many things I’m planning to improve, both
in the format design and in my implementation. Just a few of the planned
improvements:

-  Packaging oZip as a CLI tool using setuptools
-  Adding a testing suite and make sure oZip plays nice on different
   platforms
-  Optimize both speed and compression ratio
-  Adding one of the LZ flavours to improve compression ratio
-  Creating a packaged executable with a simple GUI

License
-------

This project is licensed under the GNU GPL v2.0 License. Please read the
LICENSE.txt file to learn more about the allowed usage of this project.