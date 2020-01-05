FROM ruby:2.4.1-slim

LABEL maintainer=sheldon<sreed20@asu.edu>

ENV S3_WEBSITE_VERSION  3.4.0

ARG REFRESHED_AT
ENV REFRESHED_AT $REFRESHED_AT


RUN apt-get update -qqy && apt-get -qqyy install \
    curl \
    gnupg2

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update -qqy && apt-get -qqyy install \
    nodejs \
    yarn \
  && rm -rf /var/lib/apt/lists/*
RUN apt-get update -qqy && apt-get -qqqqqqqyyyyyyy install \
    git \
	imagemagick \
	php5-imagick \
    openssh-server \
    bash \
    build-essential \
#    chromium-browser \
    openjdk-7-jdk

WORKDIR /usr/app

RUN ls

RUN gem install bundler --version 1.16.1

RUN gem install s3_website -v $S3_WEBSITE_VERSION
RUN s3_website install

RUN npm -v
RUN node -v
RUN bundler -v
