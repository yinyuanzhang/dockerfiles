FROM debian:wheezy

RUN apt-get update \
  && apt-get install -y libicu-dev subversion unzip cmake build-essential \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN set -x \
  && svn checkout http://sfntly.googlecode.com/svn/trunk/ sfntly \
  && cd sfntly/cpp/ext/redist \
  && unzip gtest-1.6.0.zip \
  && mv gtest-1.6.0 ../gtest \
  && cd ../../ \
  && mkdir build \
  && cd ./build \
  && cmake .. \
  && make

WORKDIR /sfntly
