FROM ivixq/alpine-s6-edge
MAINTAINER ivixq

RUN apk update && apk upgrade && \
    apk add --update mutt \
        msmtp \
        lynx  && \
    rm -rf /var/cache/apk/*

COPY rootfs /

#VOLUME [ "/scripts/" ]

ENTRYPOINT [ "/init" ]

CMD []

