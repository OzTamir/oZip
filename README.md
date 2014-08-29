oZip
====

## Simple compression solution in Python

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

## oZip1 Specification

The current version of oZip is actually just an implantation of the *Huffman* algorithm. The compression process starts with processing the data to create a frequency table. Next, we create a Huffman tree based on this table and encode the date using the resulted code.

At this stage we face a problem. We have an compressed data and a codebook which allows us to decode the data. However, because the compressed data can't be decoded without the codebook, we need to deliver the codebook along with the compressed file. This pose another problem - since the resulted data will be a binary string ('1's and '0's), we won't be able tell if we are reading the codebook or the compressed data.

![oZip1 Structure](http://www.poweruser.co.il/wp-content/uploads/2014/08/oZip1-Structure.png)

To solve this problem, every oZip1 archive file starts with a 32bit prefix which store the length of the codebook. In other words - the first 32bits of the archive tells the decompresser how many bits should it read to restore the codebook.


## Roadmap

Going forward there are still many things I'm planning to improve, both in the format design and in my implementation. Just a few of the planned improvements:

*   Packaging oZip as a CLI tool using setuptools
*   Adding a testing suite and make sure oZip plays nice on different platforms
*   Optimize both speed and compression ratio
*   Adding one of the LZ flavours to improve compression ratio
*   Creating a packaged executable with a simple GUI

## License
This project is licensed under the GNU GPL v2.0 License. Please read the LICENSE.txt file to learn more about the allowed usage of this project.

