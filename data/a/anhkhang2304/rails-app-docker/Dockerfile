FROM ruby:2.4.2
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
RUN ruby  --version
RUN curl -o /usr/bin/framgia-ci https://raw.githubusercontent.com/framgiaci/framgia-ci-cli/master/dist/framgia-ci \
    && chmod +x /usr/bin/framgia-ci
 
MAINTAINER Ngo Anh Khang
