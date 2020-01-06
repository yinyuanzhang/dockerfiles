FROM bellsoft/liberica-openjdk-alpine:8
LABEL maintainer="Ilshat Sultanov <just.sultanov@gmail.com>"

ENV DEPS_VERSION=1.10.0.411

WORKDIR /tmp

RUN apk add --update --no-cache bash curl rlwrap \
  --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted \
  && wget https://download.clojure.org/install/linux-install-$DEPS_VERSION.sh \
  && chmod +x linux-install-$DEPS_VERSION.sh \
  && ./linux-install-$DEPS_VERSION.sh \
  && rm -rf /tmp/* /var/cache/apk/*
