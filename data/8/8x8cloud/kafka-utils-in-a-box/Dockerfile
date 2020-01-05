FROM ubuntu:16.04
MAINTAINER Greg Feigenson "greg.feigenson@8x8.com"

RUN apt-get -qq update \
  && apt-get install -qq -y software-properties-common \
  && add-apt-repository -y ppa:fkrull/deadsnakes \
  && apt-get update -qq \
  && apt-get install -qq -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    python2.7 \
    python2.7-dev \
    python-pip \
    python-pkg-resources \
    python-setuptools \
  && pip -qqq install kafka-utils

# This image is meant to be used interactively.
CMD ["/bin/bash"]
