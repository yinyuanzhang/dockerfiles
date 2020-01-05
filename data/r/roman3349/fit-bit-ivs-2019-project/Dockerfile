FROM ubuntu:bionic

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
 && apt-get install -y antlr4 build-essential cmake devscripts doxygen fakeroot \
    git-buildpackage libgtest-dev libgtkmm-3.0-dev uuid-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
