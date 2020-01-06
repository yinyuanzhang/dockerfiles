FROM alpine:latest
LABEL Description="hugo - static site generator" Vendor="paramtamtam"

ARG HUGO_VERSION=0.60.1
ENV HUGO_VERSION="${HUGO_VERSION}"

RUN \
  mkdir -p /tmp/hugo \
  && wget "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz" \
    -O /tmp/hugo/hugo.tar.gz \
  && tar xzf /tmp/hugo/hugo.tar.gz -C /tmp/hugo \
  && mv /tmp/hugo/hugo /usr/bin \
  && rm -Rf /tmp/hugo \
  && hugo version \
  && mkdir /src

EXPOSE 1313
WORKDIR /src
VOLUME ["/src"]
ENTRYPOINT ["/usr/bin/hugo"]
