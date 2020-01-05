FROM alpine:latest
MAINTAINER Tyler Baker <forcedinductionz@gmail.com>

ARG VERSION=v3.0.0
ARG VERSION_MAJOR=v3.0.0
ARG GLIBC_VERSION=2.28-r0

ENV FILENAME swap-${VERSION_MAJOR}-cli-linux.tar.gz
ENV DOWNLOAD_URL https://github.com/swap-dev/swap/releases/download/${VERSION}/${FILENAME}

RUN apk update \
  && apk --no-cache add wget tar bash ca-certificates \
  && wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub \
  && wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk \
  && wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk \
  && apk --no-cache add glibc-${GLIBC_VERSION}.apk \
  && apk --no-cache add glibc-bin-${GLIBC_VERSION}.apk \
  && apk --no-cache add eudev-libs \
  && rm -rf /glibc-${GLIBC_VERSION}.apk \
  && rm -rf /glibc-bin-${GLIBC_VERSION}.apk \
  && wget $DOWNLOAD_URL \
  && tar xvf $FILENAME \
  && mkdir /root/.swap \
  && mv swap-${VERSION_MAJOR}-cli-linux/* /usr/local/bin/ \
  && rm -rf /swap-${VERSION_MAJOR}-cli-linux/ \
  && rm -rf /$FILENAME \
  && apk del tar wget ca-certificates

EXPOSE 19949 19950

ADD ./bin/docker_entrypoint.sh /usr/local/bin/docker_entrypoint.sh
RUN chmod a+x /usr/local/bin/docker_entrypoint.sh

ENTRYPOINT ["/usr/local/bin/docker_entrypoint.sh"]
