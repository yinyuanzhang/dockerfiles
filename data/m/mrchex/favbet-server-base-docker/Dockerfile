# Version: 0.0.1
FROM ubuntu:14.04
MAINTAINER Favbet <chex+favbet@soul.li>

ENV DEBIAN_FRONTEND noninteractive

# Installing base requirements
RUN apt-get update && apt-get install -y \
                       npm nodejs-legacy \
                       python-virtualenv python3-dev libmysqlclient-dev


RUN npm install -g coffee-script bower
ENV NODE_PATH /usr/local/lib/node_modules

RUN locale-gen "en_US.UTF-8"
RUN locale-gen "ru_RU.UTF-8"
RUN dpkg-reconfigure locales
RUN echo "export LC_ALL=en_US.utf8" >> /root/.bashrc
RUN echo "export LANG=en_US.utf8" >> /root/.bashrc
