FROM alpine:latest

RUN apk --no-cache add ca-certificates openssl curl && \
    GLIBC_PKG_VERSION=$(basename $(curl -Ls -w %{url_effective} -o /dev/null https://github.com/sgerrand/alpine-pkg-glibc/releases/latest)) && \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_PKG_VERSION}/glibc-${GLIBC_PKG_VERSION}.apk && \
    apk add glibc-${GLIBC_PKG_VERSION}.apk && \
    rm glibc-${GLIBC_PKG_VERSION}.apk && \
    apk del ca-certificates openssl curl && \
    GLIBC_PKG_VERSION=