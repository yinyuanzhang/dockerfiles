#
# Node.js w/ n version manager and JSPM Dockerfile
#

FROM debian:jessie

MAINTAINER Marko Kirves <marko.kirves@bynd.com>

ENV LANG C.UTF-8

# Install and update Debian packages
RUN apt-get update -y -q && apt-get install --no-install-recommends -y -q \
        ca-certificates \
        git \
        build-essential \
        python \
        wget \
    && rm -rf /var/lib/apt/lists/*

# Change to the latest Node.js version
ENV NODE_VERSION 0.12.7

RUN \
  cd /tmp && \
  wget http://nodejs.org/dist/v0.12.7/node-v0.12.7.tar.gz && \
  tar xvzf node-v*.tar.gz && \
  rm -f node-v*.tar.gz && \
  cd node-v* && \
  ./configure && \
  CXX="g++ -Wno-unused-local-typedefs" make && \
  CXX="g++ -Wno-unused-local-typedefs" make install && \
  cd /tmp && \
  rm -rf /tmp/node-v* && \
  npm install -g npm && \
  printf '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc  

# Install JSPM
RUN npm install -g jspm

ENV NODE_BIN /usr/local/bin/node
ENV NPM_BIN /usr/local/bin/npm
ENV JSPM_BIN /usr/local/bin/jspm

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["bash"]