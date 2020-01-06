FROM boky/alpine-bootstrap
LABEL maintainer="Bojan Cekrlic - https://github.com/bokysan/docker-alpine-bootstrap-aws/"

# Install aws-cli
RUN   \
      apk add --no-cache --update python py-pip && \
      pip install awscli --upgrade && \
      apk -v --purge del py-pip && \
      (rm "/tmp/"* 2>/dev/null || true) && (rm -rf /var/cache/apk/* 2>/dev/null || true)

