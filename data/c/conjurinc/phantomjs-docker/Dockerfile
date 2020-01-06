FROM ubuntu:14.04
MAINTAINER Conjur Inc

RUN apt-get update -y && \
		apt-get install -y software-properties-common && \
		apt-add-repository -y ppa:brightbox/ruby-ng && \
		apt-get update -y && \
		apt-get install -y \
		apt-transport-https \
		build-essential \
		ruby2.2 ruby2.2-dev \
                g++ flex bison gperf \
                perl libsqlite3-dev libfontconfig1-dev \
                libicu-dev libfreetype6 libssl-dev \
                libpng-dev libjpeg-dev python git \
                npm && \
                ln -s /usr/bin/nodejs /usr/bin/node

ADD phantomjs /opt/phantomjs
WORKDIR /opt/phantomjs
RUN ./build.sh --confirm && ln -s /opt/phantomjs/bin/phantomjs /usr/local/bin/phantomjs
