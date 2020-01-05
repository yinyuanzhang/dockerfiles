# Requires docker v17.05 or greater for multi-stage builds
# Use the golang image to build a statically-linked version of github.com/cloudflare/cfssl
# and copy this into the scratch image
FROM golang
ENV REPO=github.com/cloudflare/cfssl
ENV CLONE_URL=https://${REPO} \
    DEST=/go/src/${REPO} \
    GOPATH=/go \
    CGO_ENABLED=0 \
    GOX_OUTPUT=/build/{{.Dir}} \
    GOX_ARCH=linux/amd64 \
    GOX_LDFLAGS=-w
RUN mkdir -p /go/src/github.com/cloudflare && mkdir /build
RUN git clone ${CLONE_URL} ${DEST}
RUN go install ${REPO}/cmd/...
RUN go get github.com/mitchellh/gox
RUN go get github.com/GeertJohan/go.rice
RUN go get github.com/GeertJohan/go.rice/rice
WORKDIR ${DEST}
RUN bash -c "pushd ${DEST}/cli/serve && rice embed-go && popd" \
    && ps -ef | grep -i rice \
    && gox -osarch ${GOX_ARCH} \
        -ldflags ${GOX_LDFLAGS} \
        -output ${GOX_OUTPUT} ${REPO}/cmd/cfssl

FROM scratch
LABEL maintainer "oconnormi"

COPY --from=0 /build/cfssl /

ENTRYPOINT ["/cfssl"]
CMD ["--help"]
