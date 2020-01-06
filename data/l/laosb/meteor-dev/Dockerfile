FROM ubuntu:14.04

MAINTAINER Wexpo Lyu "laosb@lns.unihubs.com"

RUN update-locale LANG=C.UTF-8 LC_MESSAGES=POSIX

RUN apt-get update
RUN apt-get -y dist-upgrade
RUN apt-get install -y curl

RUN curl https://install.meteor.com/ | sh

WORKDIR /opt/app

EXPOSE 3000
VOLUME /opt/app

CMD [ "meteor" ]
