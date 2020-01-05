FROM alpine:3.7

ENV OAUTH2_PROXY_VERSION 2.2

RUN addgroup -g 1000 oauth_proxy \
    && adduser -u 1000 -G oauth_proxy -s /bin/sh -D oauth_proxy

# Install CA certificates
RUN apk add --no-cache --virtual=build-dependencies ca-certificates

ADD https://github.com/bitly/oauth2_proxy/releases/download/v2.2/oauth2_proxy-2.2.0.linux-amd64.go1.8.1.tar.gz /tmp

RUN tar -xf /tmp/oauth2_proxy-2.2.0.linux-amd64.go1.8.1.tar.gz -C ./bin --strip-components=1 && \
    rm /tmp/*.tar.gz

USER oauth_proxy

EXPOSE 4180
ENTRYPOINT [ "./bin/oauth2_proxy" ]
