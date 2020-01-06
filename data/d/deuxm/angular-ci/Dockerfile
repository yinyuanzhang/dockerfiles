FROM node:8.15
MAINTAINER Arne Bosien

USER root

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list
RUN apt-get update && apt-get install --no-install-recommends -y google-chrome-stable

# chrome does not like to run as root, so we create a user
RUN useradd ci --shell /bin/bash --create-home

WORKDIR /home/ci
USER ci
