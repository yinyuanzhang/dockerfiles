FROM alpine:3.8

# MhSendmail
RUN apk --no-cache add --virtual .mhsendmail curl go git musl-dev\
    && go get github.com/mailhog/mhsendmail \
    && cp /root/go/bin/mhsendmail /usr/bin/mhsendmail \
    && apk del .mhsendmail
ENTRYPOINT ["/usr/bin/mhsendmail"]