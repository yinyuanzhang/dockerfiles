# This Dockerfile is used to build an image containing basic stuff to be used as a Jenkins slave build node for Jekyll 3.1.x
# Build image with: sudo docker build -t asimio/ci-jekyll:1.0 .

FROM ubuntu:16.04
MAINTAINER Orlando L Otero <orlando.otero@asimio.net>, https://bitbucket.org/asimio/ci

VOLUME /tmp

# Update Ubuntu
RUN \
  apt-get -qq update && \
  apt-get -y upgrade && apt-get -y autoclean && apt-get -y autoremove && \
  bash -c 'DEBIAN_FRONTEND=noninteractive apt-get install -qq -y curl wget tar openjdk-8-jre \
    software-properties-common python-software-properties make locales' && \
    rm -rf /var/lib/apt/lists/*

# Set default locale for the environment
RUN \
  dpkg-reconfigure locales && \
  locale-gen --purge en_US.UTF-8 && \
  /usr/sbin/update-locale LANG=C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN \
  add-apt-repository -y ppa:brightbox/ruby-ng && \
  apt-get -qq update && \
  bash -c 'DEBIAN_FRONTEND=noninteractive apt-get -y install build-essential g++ ruby2.4 ruby2.4-dev ruby-switch zlib1g-dev' && \
  rm -rf /var/lib/apt/lists/*

RUN ruby-switch --set ruby2.4
RUN \
  gem update --system && \
  gem install jekyll && \
  gem install jekyll-paginate && \
  gem install jekyll-sitemap && \
  gem install jekyll-twitter-plugin && \
  gem install pygments.rb && \
  gem install s3_website && \
  gem install sass && \
  gem install jekyll-algolia
