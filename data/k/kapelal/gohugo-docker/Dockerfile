FROM alpine:3.6
ENV HUGO_VERSION=0.38.1
RUN \
  adduser -h /site -s /sbin/nologin -u 1000 -D hugo && \
  apk add --no-cache \
    dumb-init \
    wget \
  && wget --no-check-certificate https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz \
  && tar zxvf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz \
  && mv hugo /bin/hugo \
  && chmod +x /bin/hugo

WORKDIR /site
VOLUME  /site
EXPOSE  1313

ENTRYPOINT ["/usr/bin/dumb-init", "--", "hugo"]
