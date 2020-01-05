FROM ruby:2.6.3-slim

ENV APP_HOME /danger
WORKDIR $APP_HOME

COPY ./Gemfile $APP_HOME/Gemfile

RUN apt-get update && \
    apt-get install -y --no-install-recommends make g++ && \
    bundle install && \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false make g++ && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /usr/local/bundle/cache/* /usr/local/share/.cache/* /var/cache/* /tmp/* /var/lib/apt/lists/*