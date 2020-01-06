FROM ruby:2.3

COPY Gemfile .
COPY Gemfile.lock .

RUN gem install bundler -v '~>2' --no-document; \
    bundle
