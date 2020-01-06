FROM ubuntu:latest

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get -y install \
    git \
    python \
    python-pip

RUN pip install flawfinder
