FROM ruby:2.6

# I'm the maintainer!
MAINTAINER blambeau@enspirit.be

ENV LANG C.UTF-8
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Set correct environment variables and workdir
ENV HOME /home/app
WORKDIR /home/app

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update -qq \
 && apt-get install -qq --no-install-recommends \
    nodejs \
    yarn \
    curl \
    vim \
    default-jre \
    libsasl2-dev \
 && gem update --system && gem install bundler \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
