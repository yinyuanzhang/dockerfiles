FROM node:dubnium-alpine

WORKDIR /workdir/

RUN apk update && \
  apk -Uuv add bash \
  groff \
  less \
  python \
  py-pip && \
  pip install -q awscli==1.16.252 && \
  apk --purge -v del py-pip && \
  rm /var/cache/apk/*

ARG VERSION=local
ARG DATETIME=local;
ARG BUILD=local;
ARG COMMIT=local;

LABEL org.opencontainers.image.title="Node with AWS CLI" \
  org.opencontainers.image.description="Node image with AWS CLI. Suitable for Bitbucket pipelines." \
  org.opencontainers.image.created="$DATETIME" \
  org.opencontainers.image.version="$VERSION" \
  org.opencontainers.image.authors="daniel.jarlevang@enfo.se" \
  org.opencontainers.image.revision="build:$BUILD;commit:$COMMIT" \
  org.opencontainers.image.vendor="Enfo Sweden AB: Cloud & App Dev" \
  org.opencontainers.image.licenses="MIT"

CMD ["/bin/bash"]
