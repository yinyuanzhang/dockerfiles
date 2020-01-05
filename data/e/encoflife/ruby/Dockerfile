FROM ubuntu:14.04
MAINTAINER Dmitry Mozzherin

ENV LAST_FULL_REBUILD 2015-03-05
ENV RUBY_VERSION 1.9.3-p392
ENV RUBY_INSTALL_VERSION 0.5.0

RUN apt-get update && \
    apt-get install -y wget curl \
      build-essential git git-core \
      zlib1g-dev libssl-dev libreadline-dev \
      libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev && \
    apt-get update && \
    cd /tmp && \
    wget -O ruby-install-$RUBY_INSTALL_VERSION.tar.gz \
      https://github.com/postmodern/ruby-install/archive/v$RUBY_INSTALL_VERSION.tar.gz && \
    tar -xzvf ruby-install-$RUBY_INSTALL_VERSION.tar.gz && \
    cd ruby-install-$RUBY_INSTALL_VERSION/ && \
    make install && \
    ruby-install ruby $RUBY_VERSION && \
    apt-get autoremove -y && \
    apt-get clean py && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/local/src/*

# Add Ruby binaries to $PATH
ENV PATH /opt/rubies/ruby-$RUBY_VERSION/bin:$PATH

# Add options to gemrc
RUN echo "gem: --no-document" > ~/.gemrc

# Install bundler
RUN gem install bundler
