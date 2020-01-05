FROM alpine:latest

ENV REFRESHED_AT 2017-05-21

RUN apk add --update curl && \
  apk add --update bash && \
  rm -rf /var/cache/apk/*

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["curl"]
