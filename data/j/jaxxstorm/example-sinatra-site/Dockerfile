FROM ruby:2.3.1

MAINTAINER jaxxstorm "https://github.com/jaxxstorm"

ARG APP_VERSION=0.2

ENV APP_VERSION ${APP_VERSION}

# Install packages for building ruby
RUN gem install bundler

RUN mkdir /srv/app
ADD *.rb /srv/app/
ADD config.ru /srv/app
ADD Gemfile /srv/app
ADD Procfile /srv/app
ADD views /srv/app/views
ADD public /srv/app/public
RUN cd /srv/app; bundle install

EXPOSE 4567
WORKDIR /srv/app

CMD ["foreman","start"]
