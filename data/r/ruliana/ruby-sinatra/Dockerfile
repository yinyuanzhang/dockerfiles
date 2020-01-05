FROM ruby:2.2.5

MAINTAINER Ronie Uliana <ronie.uliana@gmail.com>

ENV RACK_ENV development

RUN mkdir -p /usr/src/app

ADD startup.sh /

WORKDIR /usr/src/app

EXPOSE 80

CMD ["/bin/bash", "/startup.sh"]
