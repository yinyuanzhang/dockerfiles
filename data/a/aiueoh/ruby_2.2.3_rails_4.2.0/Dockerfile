# === Reference ===
# Rails intall tutorial: https://gorails.com/setup/ubuntu/14.04

FROM ubuntu:14.04
MAINTAINER aiueoH

RUN useradd -m railsuser && \
    echo "railsuser ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers

USER railsuser

RUN sudo apt-get update && \
    sudo apt-get install -y \
    python-software-properties \
    software-properties-common

RUN sudo add-apt-repository ppa:chris-lea/node.js && \
    sudo apt-get update && \
    sudo apt-get install -y \
    git-core \
    curl \
    zlib1g-dev \
    build-essential \
    libssl-dev \
    libreadline-dev \
    libyaml-dev \
    libsqlite3-dev \
    sqlite3 \
    libxml2-dev \
    libxslt1-dev \
    libcurl4-openssl-dev \
    libffi-dev \
    nodejs

RUN cd && \
    git clone git://github.com/sstephenson/rbenv.git .rbenv && \
    echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc && \
    echo 'eval "$(rbenv init -)"' >> ~/.bashrc && \
    exec $SHELL

RUN git clone git://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build &&\
    echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc && \
    exec $SHELL

RUN git clone https://github.com/sstephenson/rbenv-gem-rehash.git ~/.rbenv/plugins/rbenv-gem-rehash

RUN export PATH="$HOME/.rbenv/bin:$PATH" && \
    rbenv install 2.2.3 && \
    rbenv global 2.2.3

RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc && \
    export PATH="$HOME/.rbenv/shims:$HOME/.rbenv/bin:$PATH" && \
    gem install bundler && \
    gem install rails -v 4.2.0 && \
    rbenv rehash

# Dependency for ruby gem - CarrierWave
RUN sudo apt-get install -y libmagickwand-dev

USER root
