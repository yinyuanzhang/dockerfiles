FROM alpine

MAINTAINER ops@yotpo.com

RUN apk update && apk upgrade && \
    apk add --no-cache build-base ruby ruby-bundler ruby-dev sqlite-dev

RUN gem install mailcatcher json --no-ri --no-rdoc

EXPOSE 1080
EXPOSE 1025

CMD ["mailcatcher", "-f", "--ip=0.0.0.0"]

