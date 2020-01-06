FROM alpine:3.10

ENV AWSCLI_VERSION "1.16.223"

RUN apk add python py-pip && \
    pip install awscli==$AWSCLI_VERSION && \
    apk del py-pip --purge && \
    rm -rf /var/cache/apk/*

ENTRYPOINT [ "aws" ]
