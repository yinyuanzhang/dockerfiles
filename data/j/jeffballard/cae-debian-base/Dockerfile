FROM debian:stretch

MAINTAINER Jeff Ballard <ballard@pleasepleasepleasenospamwisc.edu>

ENV TERM linux
RUN ln -fs /usr/share/zoneinfo/US/Central /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
RUN sed -i -e 's/main/main contrib non-free/g' /etc/apt/sources.list && apt-get update && apt-get -y upgrade
