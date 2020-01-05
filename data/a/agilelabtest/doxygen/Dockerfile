FROM ubuntu:14.04
MAINTAINER Bruno Delb, <brunodelb@gmail.com>

RUN apt-get update
RUN apt-get install -y doxygen graphviz
RUN apt-get install -y zip
COPY ./run-doxygen.sh /
RUN chmod +x /run-doxygen.sh
RUN mkdir /doxygen
RUN mkdir /report
ADD doxygen.tag /doxygen/
WORKDIR /src
RUN doxygen -g /doxygen/Doxyfile.sample
