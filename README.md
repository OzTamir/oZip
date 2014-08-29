# oZip - Simple compression solution
===

![Demo](https://raw2.github.com/OzTamir/oZip/master/demo.png)

## Installation
To install oZip, simply use pip:

	$ pip install ozip

If for some reason pip is unavailable (Or you're on Windows), you can install by running the following commands:

	$ git clone https://github.com/OzTamir/oZip
	$ cd oZip
	$ python setup.py install

If you have any problem with the setup process, you are welcomed to open a Issue in the project's repository.

## Usage
To compress a file run the following command:

	$ ozip -i <Path to file>

This will create a file.ext.ozip in the same path.

To decompress a file, run the following command:

	$ ozip -i <oZip File> -d

This will decompress the file in the same path.

***

## License
This project is licensed under the GNU GPL v2.0 License. Please read the LICENSE.txt file to learn more about the allowed usage of this project.

## PyPi Version
[![PyPI version](https://badge.fury.io/py/oZip.svg)](http://badge.fury.io/py/oZip)

***

# Read more
To read more about how the oZip format is structured and what is the current Roadmap for future updates and releases, please go to our [GitHub page](http://oztamir.github.io/oZip/).
