FROM ruby:2.3

RUN mkdir /examples-ms
WORKDIR /examples-ms

ADD Gemfile /examples-ms/Gemfile
ADD Gemfile.lock /examples-ms/Gemfile.lock

RUN bundle install
ADD . /examples-ms

EXPOSE 4001
