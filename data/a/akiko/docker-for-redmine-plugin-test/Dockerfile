FROM ruby:2.4.1
MAINTAINER AKIKO TAKANO / (Twitter: @akiko_pusu)

### Replace shell with bash so we can source files ###
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

### install default sys packeges ###

RUN apt-get update
RUN apt-get install -qq -y \
    vim                    \
    wget                   \
    sudo                   \
    git                    \
    mercurial              \
    sqlite3                \
    curl                   \
    build-essential        \
    libpq-dev              \
    autoconf               \
    libreadline-dev        \
    libssl-dev             \
    libxml2-dev            \
    libxslt-dev            \
    zlib1g-dev             \
    libbz2-dev

### install lts stable nodejs ###
RUN cd /tmp && wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN cd /tmp && tar xfj phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN sudo cp /tmp/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin

### get Redmine source
RUN cd /tmp && hg clone https://bitbucket.org/redmine/redmine-all redmine

RUN gem install simplecov simplecov-rcov yard --no-rdoc --no-ri
RUN gem update bundler

EXPOSE 3000

### pull changeset
WORKDIR /tmp/redmine
CMD hg pull
