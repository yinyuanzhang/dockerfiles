FROM ruby:2.6.3
RUN apt update -qq
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt install build-essential nodejs -yqq
RUN gem update --system
RUN gem install bundler
