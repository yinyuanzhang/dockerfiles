# Just creating an image with Ruby v2.2
FROM ubuntu:14.04
MAINTAINER Ash Wilson awilson@cloudpassage.com

RUN apt-get update && apt-get install -y \
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
    python-software-properties \
    libffi-dev 

COPY ./scripts/installRuby.sh /root/installRuby.sh
RUN chmod 755 /root/installRuby.sh 
RUN cd /root && ./installRuby.sh

RUN /root/.rbenv/bin/rbenv install 2.2.0
RUN /root/.rbenv/bin/rbenv global 2.2.0
