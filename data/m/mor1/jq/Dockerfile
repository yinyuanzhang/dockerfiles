FROM alpine:latest
MAINTAINER Richard Mortier <mort@cantab.net>

RUN apk --no-cache add --update                 \
        jq

WORKDIR /cwd
ENTRYPOINT ["jq"]
