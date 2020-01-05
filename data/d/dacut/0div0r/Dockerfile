FROM ubuntu:18.04
ARG REGION=us-west-2
ENV DEBIAN_FRONTEND=noninteractive
RUN sed -e "s,http://archive\.ubuntu\.com/,http://${REGION}.ec2.archive.ubuntu.com/," /etc/apt/sources.list > /etc/apt/sources.list.new && mv /etc/apt/sources.list.new /etc/apt/sources.list
RUN apt update -y
RUN apt install -y curl
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt install -y awscli build-essential git nodejs ruby ruby-dev
RUN gem install bundler
RUN gem update --system
RUN npm install -g gulp

RUN mkdir /webapp
COPY package.json package-lock.json Gemfile Gemfile.lock /webapp/
WORKDIR /webapp
RUN npm install
RUN /usr/bin/bundle2.5 install

COPY . /webapp

# Build
RUN gulp build
RUN test -f public/main.bundle.js
