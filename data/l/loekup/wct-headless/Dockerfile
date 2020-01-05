FROM ubuntu:trusty
ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

MAINTAINER Vincent Voyer <vincent@zeroload.net>
RUN apt-get -y update
RUN apt-get install -y -q software-properties-common wget
RUN add-apt-repository -y ppa:mozillateam/firefox-next

RUN wget -qO- https://deb.nodesource.com/setup_5.x | sudo bash -
RUN sudo apt-get install -y nodejs

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list
RUN apt-get update -y
RUN apt-get install -y -q \
  firefox \
  google-chrome-beta \
  default-jre \
  nodejs \
  xvfb \
  git

RUN npm install -g bower
RUN npm install -g gulp
RUN npm install -g web-component-tester