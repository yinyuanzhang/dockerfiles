FROM ruby:2.5-buster

RUN apt update && apt install nodejs postgresql-client -y && apt clean

RUN gem install bundler
# throw errors if Gemfile has been modified since Gemfile.lock
RUN bundle config --global frozen 1

WORKDIR /var/src/app

ARG RAILS_ENV=production
ENV RAILS_ENV=$RAILS_ENV
ENV RAILS_SERVE_STATIC_FILES=0
ENV RAILS_LOG_TO_STDOUT=true

COPY Gemfile Gemfile.lock ./
RUN [ "$RAILS_ENV" = "production" ] \
      && bundle install --without development test \
      || bundle install

EXPOSE 3000

# Add a script to be executed every time the container starts.
COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

COPY ./ .

RUN if [ "$RAILS_ENV" = "production" ]; then ./bin/rails assets:precompile; fi
