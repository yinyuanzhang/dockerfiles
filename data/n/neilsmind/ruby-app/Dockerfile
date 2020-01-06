FROM neilsmind/ruby-app:2.3

# throw errors if Gemfile has been modified since Gemfile.lock
RUN bundle config --global frozen 1

RUN mkdir -p /app
RUN mkdir -p /vendor
WORKDIR /app

ONBUILD COPY .ruby-version /app/
ONBUILD COPY Gemfile /app/
ONBUILD COPY Gemfile.lock /app/
ONBUILD COPY vendor/cache /app/vendor/

ONBUILD RUN bundle install

ONBUILD COPY . /app
