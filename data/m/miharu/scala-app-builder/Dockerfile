FROM ubuntu:18.04

MAINTAINER Toshiaki Inahata <inahata@miharu.co.jp>


RUN set -x \
        && apt-get update \
        && apt-get upgrade -y \
        && apt-get install -y git curl wget unzip vim \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*


# Install SBT
# ==============================================================================
RUN set -x \
        && apt-get update \
        && apt-get install -y openjdk-8-jre openjdk-8-jdk \
        \
        && wget -O- "https://github.com/sbt/sbt/releases/download/v1.2.8/sbt-1.2.8.tgz" | tar xzf - -C /usr/local --strip-components=1 \
        && sbt exit \
        \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*


# Install Node and Yarn
# ==============================================================================
RUN set -x \
        && apt-get update \
        && apt-get install -y nodejs npm \
        && npm cache clean \
        && npm install n -g \
        && n 10.16.0 \
        && ln -sf /usr/local/bin/node /usr/bin/node \
        \
        && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
        && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
        && apt-get install apt-transport-https -y \
        && apt-get update \
        && apt-get install -y yarn \
        \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*


# Install awscli
# ==============================================================================
RUN set -x \
        && apt-get update \
        && apt-get install -y python-pip python-dev \
        && pip install awscli \
        \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*


# Install Japanese
# ==============================================================================
RUN set -x \
        && apt-get update \
        && apt-get install -y language-pack-ja \
        && locale-gen ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
