FROM ruby:2.5-alpine
RUN gem install web_translate_it

RUN mkdir /data
VOLUME /data

WORKDIR /data

RUN wti -v

CMD wti pull