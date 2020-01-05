FROM balenalib/raspberry-pi2

MAINTAINER Vasyl Petrushko <vasso@gmail.com>

RUN [ "cross-build-start" ]

RUN apt-get update
RUN apt-get install -y --no-install-recommends libusb-1.0-0-dev
RUN apt-get install -y --no-install-recommends pkg-config
RUN apt-get install -y --no-install-recommends ca-certificates
RUN apt-get install -y --no-install-recommends git-core
RUN apt-get install -y --no-install-recommends cmake
RUN apt-get install -y --no-install-recommends build-essential

RUN [ "cross-build-end" ]
