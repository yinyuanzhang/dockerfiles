FROM alpine:latest
MAINTAINER IF Fulcrum "fulcrum@ifsight.net"

ENV NPM_CONFIG_LOGLEVEL=info
ENV NODE_VERSION=6.10.3
ENV NODE_PATH=/usr/lib/node_modules

RUN apk --no-cache add nodejs

ENTRYPOINT ["/usr/bin/node"]
