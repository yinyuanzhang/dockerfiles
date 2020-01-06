# Docker configuration file to build an image for creating lots of files

FROM alpine

# Need to add python 2.7 and pip

RUN apk add --update python
RUN apk add py-pip
RUN apk add python2-dev
RUN apk add bash

# Create a "project" directory

RUN mkdir -p /usr/local/create_files/bin
RUN mkdir -p /usr/local/create_files/conf
RUN mkdir -p /usr/local/create_files/logs

# Before we can load the pip libraries, we need the GCC compiler

RUN apk add build-base

# Copy in the executables

WORKDIR /usr/local/create_files/bin
COPY create_files.py requirements.txt /usr/local/create_files/bin/

# Load all of the required pip libraries

RUN pip install -r requirements.txt

# Copy in the configuration files

WORKDIR /usr/local/create_files/conf
COPY *.yml /usr/local/create_files/conf/

# Command line parameters

CMD ["./create_files.py"]

