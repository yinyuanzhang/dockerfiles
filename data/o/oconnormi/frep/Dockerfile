# Requires docker v17.05 or greater for multi-stage builds
# Use the golang image to build a statically-linked version of github.com/subchen/frep
# and copy this into the scratch image
FROM golang
ENV FREP_VERSION=1.2.0
ENV FREP_REPO_URL=https://github.com/subchen/frep.git
ENV FREP_DEST=/go/src/github.com/subchen/frep
RUN mkdir -p /go/src/github.com/subchen && mkdir /build
RUN git clone ${FREP_REPO_URL} ${FREP_DEST}
RUN go get github.com/mitchellh/gox
WORKDIR /go/src/github.com/subchen/frep
RUN git checkout v${FREP_VERSION} -b ${FREP_VERSION} && rm -rf Makefile
COPY Makefile.frep Makefile
RUN make

FROM scratch
LABEL maintainer "oconnormi"

COPY --from=0 /build/frep_linux_amd64 /frep

VOLUME /in /out
WORKDIR /in
ENTRYPOINT ["/frep"]
CMD ["--help"]
