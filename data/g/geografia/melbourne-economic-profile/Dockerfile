FROM ruby:2.3.1-slim

ENV RAILS_ROOT=/usr/app/melb_econ
ENV RAILS_ENV=production
ENV RACK_ENV=production
ENV PGPASSWORD=lv2e8uQz3/M=
ENV POSTGRES_PASSWORD=lv2e8uQz3/M=
ENV SECRET_KEY_BASE=844e93f4e05f9621a2326fdfac8189241d67a07eda283d9658a3513e67ed09486c82143f5c18a786bbc6ae1488bcd0b1ca916c263f5646976ed25bceb65a599b
ENV RAILS_LOG_TO_STDOUT=true
ENV APP_NAME=melb_econ

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev postgresql-client libproj-dev nodejs

# Dependencies for rgeo
RUN apt-get --no-install-recommends -y install libgeos-dev libproj-dev
# Add libgeos symlinks for rgeo gem to be able to find it
RUN ln -sf /usr/lib/libgeos-3.4.2.so /usr/lib/libgeos.so && ln -sf /usr/lib/libgeos-3.4.2.so /usr/lib/libgeos.so.1

RUN mkdir -p $RAILS_ROOT/tmp/pids
WORKDIR $RAILS_ROOT

COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock

RUN bundle check || bundle install --without development test -j4

COPY config/puma.rb config/puma.rb

COPY . .

RUN mkdir -p /etc/nginx/conf.d/
COPY ./containers/production/nginx.conf /etc/nginx/conf.d/default.conf

RUN DB_ADAPTER=nulldb bundle exec rake assets:precompile RAILS_ENV=production

EXPOSE 3000
