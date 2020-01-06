
FROM alpine
LABEL MAINTAINER="Justus Luthy <jluthy@coinlion.com>"

ENV KUBECTL_VERSION="v1.9.3"

RUN \
  apk add --update ca-certificates && \
  apk add -t deps curl && \
  apk add bash

RUN \
  curl -Lo /usr/local/bin/kubectl \
    https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl && \
  chmod +x /usr/local/bin/kubectl && \
  apk del --purge deps && \
  rm /var/cache/apk/*

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
