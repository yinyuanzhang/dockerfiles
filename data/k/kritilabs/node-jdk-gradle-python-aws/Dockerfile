FROM openjdk:8u151-jdk-alpine
MAINTAINER Kritilabs <contact@kritilabs.com>

######################################## node:8.9.4 INSTALLATION STARTS ######################################################
ENV NODE_VERSION 8.9.4

RUN addgroup -g 1000 node \
  && adduser -u 1000 -G node -s /bin/sh -D node \
  && apk add --no-cache \
    binutils-gold curl g++ gcc git gnupg libgcc libstdc++ linux-headers make python python-dev \
  # gpg keys listed at https://github.com/nodejs/node#release-team
  && for key in \
    77984A986EBC2AA786BC0F66B01FBB92821C587A \
  ; do \
    gpg --keyserver pgp.mit.edu --recv-keys "$key" || \
    gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \
  done \
    && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.xz" \
    && curl -SLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
    && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
    && grep " node-v$NODE_VERSION.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
    && tar -xf "node-v$NODE_VERSION.tar.xz" \
    && cd "node-v$NODE_VERSION" \
    && ./configure \
    && make -j$(getconf _NPROCESSORS_ONLN) \
    && make install \
    && cd .. \
    && rm -Rf "node-v$NODE_VERSION" \
    && rm "node-v$NODE_VERSION.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
######################################## node:8.9.4 INSTALLATION ENDS ######################################################

######################################## GRADLE INSTALLATION STARTS ######################################################
RUN mkdir /usr/lib/gradle /app

ENV GRADLE_VERSION 4.10.3
ENV GRADLE_HOME /usr/lib/gradle/gradle-${GRADLE_VERSION}
ENV PATH ${PATH}:${GRADLE_HOME}/bin

WORKDIR /usr/lib/gradle
RUN set -x \
  && apk add --no-cache wget \
  && wget https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \
  && unzip gradle-${GRADLE_VERSION}-bin.zip \
  && rm gradle-${GRADLE_VERSION}-bin.zip \
  && apk del wget

######################################## GRADLE INSTALLATION ENDS ######################################################

RUN apk --no-cache update && \
    apk --no-cache add python py-pip py-setuptools ca-certificates curl groff less zip bash libstdc++ jq && \
    pip --no-cache-dir install --upgrade --user awscli && \
    pip --no-cache-dir install --upgrade --user awsebcli && \
    pip --no-cache-dir install --upgrade --user boto3 && \
    rm -rf /var/cache/apk/*

RUN apk update && \
    apk add --no-cache git openssh perl && \
    pip install pytz tzlocal
ENV PATH "$PATH:~/.local/bin"

ADD deployment-scripts /opt/deployment-scripts
