FROM python:3.6-stretch
MAINTAINER haakenlid
WORKDIR /
RUN   apt-get update && \
      apt-get install -y \
      build-essential \
      cmake \
      libtbb2 \
      libtbb-dev \
      libjpeg-dev \
      libpng-dev \
      libtiff-dev \
      pkg-config \
&& rm -rf /var/lib/apt/lists/*

RUN   pip install numpy
COPY  makeopencv.sh ./
RUN   ["./makeopencv.sh", "3.3.1"]
