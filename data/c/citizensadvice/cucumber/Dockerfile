FROM ruby:2.5.1

ADD Gemfile* /tests/
WORKDIR /tests
RUN gem install bundler && bundle install -j3 && bundle clean

ADD . /tests/

