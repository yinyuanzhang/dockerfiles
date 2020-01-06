FROM ruby:2.2

RUN apt-get update -qq
RUN apt-get install -y libpq-dev libxml2-dev libxslt1-dev nodejs

COPY . /srv/pothibo.com
WORKDIR /srv/pothibo.com

ENV RAILS_ENV production

RUN bundle install --deployment --path=.bundle

EXPOSE 3000
