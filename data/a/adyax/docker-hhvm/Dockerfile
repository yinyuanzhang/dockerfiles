# Docker Adyax
#
#

FROM debian:wheezy

MAINTAINER Benoît GRUNENBERGER <bgrunenberger@adyax.com>

ENV DEBIAN_FRONTEND noninteractive


RUN apt-get update -y && \
      apt-get install -y wget && \
      apt-get update -y && \
      wget -O - http://dl.hhvm.com/conf/hhvm.gpg.key | apt-key add - && \
      echo deb http://dl.hhvm.com/debian wheezy main | tee /etc/apt/sources.list.d/hhvm.list && \
      apt-get update -y && \
      apt-get install -y hhvm && \
      apt-get -y -q autoclean && \
      apt-get -y -q autoremove

ADD php.ini /etc/hhvm/php.ini
ADD server.ini /etc/hhvm/server.ini

EXPOSE 9000

ENTRYPOINT ["hhvm"]

#CMD /etc/init.d/hhvm start &
