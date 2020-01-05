FROM starefossen/ruby-node:alpine

LABEL maintainer="Ian Hattendorf <ian@ianhattendorf.com>"

ENV HUGO_VERSION 0.37
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux-64bit
ENV JDK_VERSION 8

RUN apk --no-cache add py-pygments git "openjdk$JDK_VERSION"

ADD https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz /usr/local/
RUN tar xzf /usr/local/${HUGO_BINARY}.tar.gz -C /usr/local/bin/ && rm /usr/local/${HUGO_BINARY}.tar.gz

RUN gem install s3_website
