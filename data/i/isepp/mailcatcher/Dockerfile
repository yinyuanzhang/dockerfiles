# A slim container for Mailcatcher
FROM ruby:2.3.3-alpine
MAINTAINER kristen.gilden@i-smith.ee

RUN set -xe \
  && apk add --no-cache --virtual .build-deps \
    sqlite \
    sqlite-dev \
    g++ \
    make \
  && gem install mailcatcher -v 0.6.5 --no-ri --no-rdoc \
  && runDeps="$( \
    scanelf --needed --nobanner --recursive /usr/local \
      | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
      | sort -u \
      | xargs -r apk info --installed \
      | sort -u \
  )" \
  && apk add --no-cache --virtual .mailcatcher-rundeps $runDeps \
  && apk del .build-deps

# smtp port
EXPOSE 1025

# webserver port
EXPOSE 1080

CMD ["mailcatcher", "-f", "--ip=0.0.0.0"]
