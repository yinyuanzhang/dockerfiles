FROM alpine as Source

WORKDIR /

RUN apk update && \
apk upgrade && \
apk add git make curl wget bash ruby ruby-bundler \
ruby ruby-bigdecimal ruby-bundler ca-certificates \
ruby-dev build-base ruby-webrick ruby-nokogiri ruby-json \
libxml2-dev libxslt-dev libffi-dev

FROM Source as Build

RUN git clone --depth=1 https://github.com/microservices-community/microservices-conf.git /git
WORKDIR /git/website
RUN make all-docker

FROM jolielang/leonardo
ENV LEONARDO_WWW /web
COPY --from=Build /git/website/_site $LEONARDO_WWW