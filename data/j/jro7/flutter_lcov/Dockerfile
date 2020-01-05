FROM ubuntu:latest

MAINTAINER jeroenroosenboom@gmail.com

WORKDIR /

RUN apt-get update && \
    apt-get install -y lcov git-core curl unzip libglu1 && \
    git clone --branch v1.10.14 --depth=1 https://github.com/flutter/flutter.git && \
    /flutter/bin/flutter doctor && \
    apt-get remove -y curl unzip && \
    apt autoremove -y && \
    rm -rf /var/lib/apt/lists/*

ENV PATH $PATH:/flutter/bin/cache/dart-sdk/bin:/flutter/bin
