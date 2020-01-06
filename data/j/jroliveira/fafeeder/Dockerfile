FROM ubuntu:19.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt update -y
RUN apt install -y wget git build-essential debhelper tcl8.6-dev autoconf python3-dev python3-venv dh-systemd libz-dev libboost-system-dev libboost-program-options-dev libboost-regex-dev libboost-filesystem-dev

RUN git clone https://github.com/flightaware/piaware_builder.git
RUN piaware_builder/sensible-build.sh stretch
COPY cxfreeze.patch /
RUN patch /piaware_builder/package-stretch/cx_Freeze-5.1.1/cx_Freeze/freezer.py /cxfreeze.patch
WORKDIR /piaware_builder/package-stretch
RUN dpkg-buildpackage -b
RUN apt install -y ../piaware_*.deb

WORKDIR /
COPY start.sh /
RUN chmod +x /start.sh

ENTRYPOINT ["/start.sh"]