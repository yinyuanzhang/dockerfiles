# Build this image: docker build -f .\Dockerfile -t illagrenan/psqlclient .
FROM alpine:latest

RUN apk add --purge --no-cache --update \
      postgresql-client
CMD [ "psql" ]
