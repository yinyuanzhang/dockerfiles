# NolimitID docker images with nodesource's trusty,
# nodejs v5.1.0, phantomjs 1.9.8, karma-cli, mocha,
# and webpack.

FROM nodesource/trusty:5.1.0

MAINTAINER maman <achmad@mahardi.me>

# Set ENV
ENV NODE_ENV dev
ENV PHANTOMJS_VERSION 1.9.8
ENV UV_THREADPOOL_SIZE=6

# Commands
RUN \
  apt-get update && \
  apt-get upgrade -y --force-yes && \
  apt-get install -y --force-yes wget curl ca-certificates libfreetype6 libfontconfig bzip2 rsync ssh && \
  mkdir -p /srv/var && \
  wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \
  tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \
  rm -rf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \
  mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \
  ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs && \
  apt-get autoremove -y && \
  apt-get clean all && \
  npm install webpack && \
  npm install karma-cli && \
  npm install dalek-cli && \
  npm install mocha
