FROM ruby:2.2.4

RUN mkdir /app
WORKDIR /app

COPY . /app

RUN gem install bundler -v 1.15 && bundle install && gem build kate-cli.gemspec && gem install kate-cli*.gem
