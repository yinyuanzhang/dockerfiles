FROM ubuntu:16.04

RUN apt-get -y update && apt-get install -y tesseract-ocr libtesseract-dev libleptonica-dev python3-pip

RUN pip3 install --upgrade pip

RUN pip3 install pillow ipython Cython

RUN pip3 install tesserocr scipy scikit-image matplotlib
