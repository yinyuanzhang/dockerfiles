FROM mhart/alpine-node:12

RUN mkdir -p /srv
WORKDIR /srv
RUN apk --update add --no-cache bash && \
  apk --update add --no-cache --virtual build-dependencies python git make g++
EXPOSE 3333
