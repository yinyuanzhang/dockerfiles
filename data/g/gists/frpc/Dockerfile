FROM alpine:3.11

ARG VERSION=0.30.0

LABEL maintainer="zgist" \
        org.label-schema.name="frpc" \
        org.label-schema.version=$VERSION

# Let's roll
RUN set -xe && \
    apk add \
        --no-cache \
        --virtual .build-deps \
        curl \
        git \
        build-base \
        go \
        upx && \
    mkdir -p /tmp/frp && cd /tmp/frp && \
    curl -sSL https://github.com/fatedier/frp/archive/v$VERSION.tar.gz | \
    tar xz --strip 1 && \
    go mod download && \
    go build -v -ldflags "-s -w" -o /usr/bin/frpc ./cmd/frpc && \
    cp ./conf/frpc.ini /etc/ && \
    cd / && upx --best /usr/bin/frpc && \
    rm -rf /root/go /root/.cache /root/.ash_history /tmp/frp && \
    apk del .build-deps

CMD ["/usr/bin/frpc", "-c", "/etc/frpc.ini"]
