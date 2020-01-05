FROM node:10.15.3-stretch-slim

WORKDIR /home/node

# We need sudo for the things
RUN apt-get -qq update && apt-get -qq -y install sudo

# Installing some missing but critical items:
# Chromium info: https://www.chromium.org/
RUN apt-get update  \
  && apt-get install -qq -y libglib2.0-0 libnss3 libx11-6 \
  && apt install -qq -y chromium

# Copies code over to the default working directory:
# The below COPY assumes you are copying /ui-tests to /ui-tests
COPY . .

# Install testing dependencies (Nightwatch, Chromedriver)
# The npm i --quiet assumes the /ui-tests directory is where it is being run from
# FYI: npm i chromedriver uses the version # from package.json
RUN sudo npm i --quiet \
  && sudo npm i -g nightwatch@0.9.21 --quiet \
  && sudo npm i -g chromedriver@73.0.0 --unsafe-perm=true --allow-root --quiet

# Moves to the directory we plan to run Nightwatch from
# WORKDIR /home/node/sedna-portal/ui-tests

# Sets variable used in Nightwatch Reporter:
ENV TEST_ENV=docker
ENV TERM=xterm-256color

RUN apt-get clean \
  && rm -rf \
    /tmp/* \
    /usr/share/doc/* \
    /var/cache/* \
    /var/lib/apt/lists/* \
    /var/tmp/*

# Check the installed version of Chromium
RUN sudo dpkg-query -l "*chromium*"