FROM node:4.4.7

ENV EMBER_CLI_VERSION 2.7.0
ENV BOWER_VERSION 1.7.9
ENV PHANTOMJS_VERSION 2.1.7
ENV WATCHMAN_VERSION 3.5.0

# Note: npm is v2.15.8
RUN \
  npm install -g ember-cli@$EMBER_CLI_VERSION && \
  npm install -g bower@$BOWER_VERSION && \
  npm install -g phantomjs-prebuilt@$PHANTOMJS_VERSION

# install watchman
RUN \
  git clone https://github.com/facebook/watchman.git && \
  cd watchman && \
  git checkout v$WATCHMAN_VERSION && \
  ./autogen.sh && \
  ./configure && \
  make && \
  make install && \
  cd .. && \
  rm -r watchman

# initialize ember application
RUN \
  ember new dvlptremberapp && \
  mkdir dvlptremberapp-cp && \
  cd /dvlptremberapp && \
  cp -r `ls -A | grep -vE "(node_modules|bower_components|.git)"` /dvlptremberapp-cp/

WORKDIR /dvlptremberapp
