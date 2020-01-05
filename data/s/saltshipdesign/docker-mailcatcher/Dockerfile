FROM alpine:3.3

RUN apk add --no-cache ca-certificates ruby ruby-bigdecimal ruby-sqlite tzdata libstdc++ \
  && apk add --no-cache -t build ruby-dev build-base \
  && gem install --no-ri --no-rdoc json \
  && gem install --no-ri --no-rdoc mailcatcher -v 0.5.12 \
  && apk del --purge build \
  && rm -rf /var/cache/apk/*

EXPOSE 1080 1025

ENTRYPOINT ["mailcatcher"]
CMD ["--smtp-ip=0.0.0.0", "--http-ip=0.0.0.0", "--foreground"]
