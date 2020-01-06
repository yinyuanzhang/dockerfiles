FROM gcc:8

RUN echo "deb http://ftp.debian.org/debian stretch-backports main" > /etc/apt/sources.list.d/stretch-backports.list \
  && apt-get update && apt-get -t stretch-backports install -y --no-install-recommends \
         doxygen ttf-freefont graphviz \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/stretch-backports.list \
  && curl https://cmake.org/files/v3.12/cmake-3.12.3-Linux-x86_64.sh -o /tmp/curl-install.sh \
  && chmod u+x /tmp/curl-install.sh \
  && mkdir /usr/bin/cmake \
  && /tmp/curl-install.sh --skip-license --prefix=/usr \
  && rm /tmp/curl-install.sh \
  && git clone https://github.com/linux-test-project/lcov.git \
  && cd lcov \
  && git checkout 94eac0e \
  && make install \
  && cd .. \
  && rm -Rf lcov
