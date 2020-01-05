FROM eadz/ubuntu-trusty-base:latest

MAINTAINER _@eaden.net

RUN apt-get update && apt-get upgrade -y && apt-get install wget build-essential libssl-dev libxslt-dev libxml2-dev -y
RUN wget http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz
RUN tar -zxf ruby-2.1.2.tar.gz
RUN cd ruby-2.1.2 && ./configure --prefix=/usr/local && make && make install
RUN rm ruby-2.1.2.tar.gz
RUN mkdir src && mv ruby-2.1.2 src
RUN gem install bundler

