FROM ubuntu:14.04

RUN apt-get update && \
    apt-get install build-essential curl git -y

# Nodejs install.
# 
# Snatched from https://hub.docker.com/_/node/ 
# and https://github.com/nodejs/docker-node/blob/bb89224e0f2572e4894c50abfa8174ca65d6b28f/4.2/Dockerfile
#
# gpg keys listed at https://github.com/nodejs/node
RUN set -ex \
  && for key in \
    9554F04D7259F04124DE6B476D5A82AC7E37093B \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
  ; do \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
  done

ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 4.2.4

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --verify SHASUMS256.txt.asc \
  && grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc | sha256sum -c - \
  && tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc

# Add global npm packages.
RUN npm install -g npm
RUN npm install -g yo@1.1.0
RUN npm install -g generator-karma@~0.5.0
RUN npm install -g generator-express-angular
#RUN npm install -g bower
#RUN npm install -g grunt-cli
#RUN npm install -g compass

COPY ./scripts/user-add.sh /root/user-add.sh
RUN chmod u+x /root/user-add.sh

# Extra run to create new build.
RUN touch /build-version.txt \
  && echo "Version: 0.1-dev5" > /build-version.txt

ENTRYPOINT bash