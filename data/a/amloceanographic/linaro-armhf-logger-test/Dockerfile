# Use Ubuntu 18.04 base image
FROM ubuntu:18.04

# Install Linaro ARM toolchain
WORKDIR /opt
RUN apt-get update && apt-get install -y curl \
  make \
  mercurial \
  unzip \
  wget \
  xz-utils
RUN wget https://releases.linaro.org/components/toolchain/binaries/6.3-2017.02/arm-linux-gnueabihf/gcc-linaro-6.3.1-2017.02-x86_64_arm-linux-gnueabihf.tar.xz
RUN tar -xf gcc-linaro-6.3.1-2017.02-x86_64_arm-linux-gnueabihf.tar.xz
RUN rm -f gcc-linaro-6.3.1-2017.02-x86_64_arm-linux-gnueabihf.tar.xz
ENV PATH="${PATH}:/opt/gcc-linaro-6.3.1-2017.02-x86_64_arm-linux-gnueabihf/bin"

RUN apt-get remove -y wget xz-utils
RUN apt-get autoremove -y
