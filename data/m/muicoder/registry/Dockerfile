FROM muicoder/glibc:golang AS build

ARG REPO="github.com/docker/distribution"
ARG DOCKER_BUILDTAGS="include_oss include_gcs"

RUN apk --no-cache add make && \
    go get -d $REPO && \
    go get github.com/golang/lint/golint && \
    make --directory $GOPATH/src/$REPO PREFIX=/usr/local clean binaries && \
    mkdir -p /etc/docker/registry && cp -v $GOPATH/src/$REPO/cmd/registry/config-example.yml /etc/docker/registry/config.yml && \
    rm -rf $GOPATH/{src,bin,pkg}/*

FROM muicoder/glibc

COPY --from=build /usr/local/bin/* /usr/local/bin/
COPY --from=build /etc/docker/registry/config.yml /etc/docker/registry/config.yml

VOLUME ["/var/lib/registry"]

EXPOSE 5000

CMD ["registry", "serve", "/etc/docker/registry/config.yml"]
