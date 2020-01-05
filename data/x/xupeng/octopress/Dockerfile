FROM debian:wheezy
MAINTAINER xupeng

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
		locales \
		ruby1.9.3 \
		rsync \
		openssh-client \
		build-essential \
		vim-nox \
		python2.7 \
		sudo \
	&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN sed -i -e 's/^# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/g' /etc/locale.gen && locale-gen en_US en_US.UTF-8
RUN ln -s /usr/bin/python2.7 /usr/bin/python
ENV LC_ALL en_US.utf8

VOLUME ["/src"]
WORKDIR /src

# Copied from octopress repo
ADD Gemfile /src/Gemfile
ADD Gemfile.lock /src/Gemfile.lock
RUN gem1.9.3 install bundler && bundler install

ADD wrapper /wrapper
