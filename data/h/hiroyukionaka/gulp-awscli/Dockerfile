# Pull base image.
FROM node:7.5
MAINTAINER Hiroyuki Onaka

RUN apt-get -y update

# Install Bower & Gulp
RUN npm install -g bower gulp

RUN apt-get -y install python-dev python-pip

RUN pip install awscli

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["bash"]
