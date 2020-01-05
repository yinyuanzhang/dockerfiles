FROM alpine:3.6

ENV GOPATH=/usr

RUN build_deps="curl go alpine-sdk" && \
    apk add -U dumb-init $build_deps && \
    go get -v -u github.com/NebulousLabs/Sia/... && \
    apk del $build_deps && \
    rm -r /usr/src /var/cache/apk/*

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
