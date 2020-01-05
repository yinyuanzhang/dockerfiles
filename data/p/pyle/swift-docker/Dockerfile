FROM ubuntu:14.04
MAINTAINER Adam Pyle <adam.pyle@griffithuni.edu.au>
RUN apt-get update --fix-missing
RUN apt-get install -y wget git cmake ninja-build clang uuid-dev \
libicu-dev icu-devtools libbsd-dev libedit-dev libxml2-dev \
libsqlite3-dev swig libpython-dev libncurses5-dev pkg-config

RUN rm -rf /var/lib/apt/lists/*
RUN wget -q https://swift.org/builds/swift-2.2-branch/ubuntu1404/swift-2.2-SNAPSHOT-2016-03-01-a/swift-2.2-SNAPSHOT-2016-03-01-a-ubuntu14.04.tar.gz -O swift.tar.gz
RUN mkdir -p /app/
RUN tar -zxf swift.tar.gz && mv swift**/ /app/swift && rm -r /swift.tar.gz
RUN echo "PATH=/app/swift/usr/bin/:\"${PATH}\"" >> /root/.bashrc
