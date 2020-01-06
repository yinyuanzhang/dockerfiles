FROM ruby:latest

WORKDIR /jekyll

COPY Gemfile* ./
RUN bundle install
RUN gem install json

ENTRYPOINT ["/usr/local/bundle/bin/jekyll"]
