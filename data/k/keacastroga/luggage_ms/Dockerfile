FROM ruby:2.6.0
RUN gem install bundler -v 2.0.0.pre1
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
RUN mkdir /myapp
WORKDIR /myapp
#COPY Gemfile.lock /myapp/Gemfile.lock

COPY . /myapp
RUN bundle install
WORKDIR /myapp
EXPOSE 4004