oZip
====

## Simple compression solution in Python

![Example](https://raw2.github.com/OzTamir/oZip/master/demo.png)

## Usage
To compress a file run the following command:

	$ python cli.py -i <Path to file>

This will create a file.ext.ozip in the same path.

To decompress a file, run the following command:

	$ python cli.py -i <oZip File> -d

This will decompress the file in the same path.

## To-Do:
 - Add LZ77 compression for even better performance (See branch LZ)
 - Make sure it works with various file types
 - **Optimize!!!**
 - Test for cross-platform support (currently tested only on OSX)
 - Add a simple GUI using [Gooey](https://github.com/chriskiehl/Gooey)
