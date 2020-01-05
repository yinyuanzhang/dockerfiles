FROM alpine:3.7

ENV KLAR_VER=2.0.2

ADD https://github.com/optiopay/klar/releases/download/v${KLAR_VER}/klar-${KLAR_VER}-linux-amd64 /usr/bin/klar
ADD entrypoint.sh /

RUN apk add --update ca-certificates \
    && chmod a+x /usr/bin/klar entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
