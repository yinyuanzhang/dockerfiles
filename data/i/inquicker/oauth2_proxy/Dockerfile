FROM alpine

ENTRYPOINT ["/usr/local/bin/oauth2_proxy"]

RUN set -ex && \
    apk add --no-cache --virtual .deps curl tar && \
    curl -Ls -o oauth2_proxy.tar.gz https://github.com/bitly/oauth2_proxy/releases/download/v2.1/oauth2_proxy-2.1.linux-amd64.go1.6.tar.gz && \
    tar -zxf oauth2_proxy.tar.gz --strip-components=1 && \
    mv oauth2_proxy /usr/local/bin/ && \
    rm oauth2_proxy.tar.gz && \
    apk del .deps && \
    apk add --no-cache ca-certificates
