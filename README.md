# Digital Watermarking

## Setup

The first thing to do is to clone the repository:

```console
$ git clone https://github.com/florianraabe/digital-watermarking.git
$ cd digital-watermarking
```

Create a virtual environment to install dependencies in and activate it:

```console
$ python -m venv venv
$ source venv/bin/activate
```

Then install the dependencies:

```console
(venv) $ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies, you can run the application:

```console
(venv) $ ./main.py
```

## Usage

The application offers the following functionality. 

### Encode

To encode a message into an image, simply specify the method and supply the path to the image as well as the message.

```console
usage: main.py encode [-h] {lsb,lsb-image,dwtDct,dwtDctSvd,rivaGan,lib3} filename message
```

The watermarked image will be in the same directory and its path will be printed.

### Decode

To decode a watermark from an image, simply specify the method and supply the path to the image.

```console
usage: main.py decode [-h] {lsb,lsb-image,dwtDct,dwtDctSvd,rivaGan,lib3} filename
```

## Tests

The tests can be found in tests.py. They use the image manipulation functionality implemented in manipulation.py. 
You can run them with the following command:

```console
(venv) $ python tests.py
```

You can also run tests for a single method. Just specify one of the following methods:

```console
(venv) $ python tests.py {TestLibrary1,TestLibrary2a,TestLibrary2b,TestLibrary2c,TestLibrary3}
```

TestLibrary1 - LSB

TestLibrary2a- dwtDct

TestLibrary2b - dwtDctSvd

TestLibrary2c - rivaGan

TestLibrary3 - lib3
