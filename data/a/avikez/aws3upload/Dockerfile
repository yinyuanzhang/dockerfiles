FROM ruby:2.4.0-alpine
MAINTAINER avikez@gmail.com

WORKDIR /app
RUN gem install aws3upload

ENTRYPOINT ["aws3upload"]
