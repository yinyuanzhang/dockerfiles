# Build:
# docker build -t meanjs/mean -f Dockerfile-production .
#
# Run:
# docker run -it meanjs/mean
#
# Compose:
# docker-compose -f docker-compose-production.yml up -d

FROM ubuntu:latest
MAINTAINER andrea@monema.it

# 80 = HTTP, 443 = HTTPS, 3000 = MEAN.JS server, 35729 = livereload
EXPOSE 80 443 3000 35729

# Install Utilities
RUN apt-get update -q  \
 && apt-get install -yqq curl \
 wget \
 ghostscript \
 aptitude \
 htop \
 vim \
 git \
 traceroute \
 dnsutils \
 curl \
 ssh \
 tree \
 tcpdump \
 nano \
 psmisc \
 gcc \
 make \
 build-essential \
 python \
 libfreetype6 \
 libfontconfig \
 libkrb5-dev \
 ruby \
 sudo \
 apt-utils \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install nodejs
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
RUN sudo apt-get install -yq nodejs \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install gem sass for grunt-contrib-sass
RUN gem install sass

# Install MEAN.JS Prerequisites
RUN npm install --quiet -g grunt-cli gulp bower yo mocha karma-cli pm2 && npm cache clean

RUN mkdir -p /opt/app/public/lib
WORKDIR /opt/app


# Copies the local package.json file to the container
# and utilities docker container cache to not needing to rebuild
# and install node_modules/ everytime we build the docker, but only
# when the local package.json file changes.
# Install npm packages
ADD package.json /opt/app/package.json
RUN NODE_ENV=development npm install --quiet

# Manually trigger bower.
ADD .bowerrc /opt/app/.bowerrc
ADD bower.json /opt/app/bower.json
RUN bower install --quiet --allow-root --config.interactive=false

