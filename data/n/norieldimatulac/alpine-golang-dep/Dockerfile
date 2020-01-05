FROM billyteves/alpine:3.5.0

MAINTAINER Noriel Dimatulac <norieldimatulac@gmail.com>

# set up nsswitch.conf for Go's "netgo" implementation
# - https://github.com/golang/go/blob/go1.9.1/src/net/conf.go#L194-L275
# - docker run --rm debian:stretch grep '^hosts:' /etc/nsswitch.conf
RUN [ ! -e /etc/nsswitch.conf ] && echo 'hosts: files dns' > /etc/nsswitch.conf

ENV GOLANG_VERSION      1.9.7
ENV GOLANG_SRC_URL      https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz
ENV GOLANG_SRC_SHA256   582814fa45e8ecb0859a208e517b48aa0ad951e3b36c7fff203d834e0ef27722
ENV GOPATH              /go
ENV PATH                $GOPATH/bin:/usr/local/go/bin:$PATH

# ssh for dep
COPY ./run-ssh /usr/local/bin/run-ssh

# make-sure-R0-is-zero-before-main-on-ppc64le.patch: https://github.com/golang/go/commit/9aea0e89b6df032c29d0add8d69ba2c95f1106d9 (Go 1.9)
# https://golang.org/issue/14851
COPY ./patch-files/*.patch /go-alpine-patches/

RUN set -ex \
    && apk add --no-cache ca-certificates \
    && apk update --no-cache \
    && apk upgrade --no-cache \
    && apk add --no-cache --virtual .build-deps \

    make \
    gcc \
    musl-dev \
    go \

# set GOROOT_BOOTSTRAP such that we can actually build Go
    && export GOROOT_BOOTSTRAP="$(go env GOROOT)" \
# ... and set "cross-building" related vars to the installed system's values so that we create a build targeting the proper arch
# (for example, if our build host is GOARCH=amd64, but our build env/image is GOARCH=386, our build needs GOARCH=386)
    && export GOOS="$(go env GOOS)" \
    && export GOARCH="$(go env GOARCH)" \
    && export GOHOSTOS="$(go env GOHOSTOS)" \
    && export GOHOSTARCH="$(go env GOHOSTARCH)" \
    && curl -L "$GOLANG_SRC_URL" > go.tar.gz \
	&& echo "$GOLANG_SRC_SHA256  go.tar.gz" | sha256sum -c - \
	&& tar -C /usr/local -xzf go.tar.gz \
	&& rm go.tar.gz \
	&& cd /usr/local/go/src \
	&& for p in /go-alpine-patches/*.patch; do \
		[ -f "$p" ] || continue; \
		patch -p2 -i "$p"; \
	done \
	&& ./make.bash \
	&& rm -rf /go-alpine-patches \
	&& apk del .build-deps \

    # Install needed apks

    && apk add --no-cache --virtual --update \
    git \
    make \
    tzdata \

    # Make directories

    && mkdir -p $GOPATH/bin \
    && mkdir -p $GOPATH/src \

    # CHMOD

    && chmod -R 777 $GOPATH \
    && chmod +x /usr/local/bin/run-ssh \

    # Go dep!
    && go get -u github.com/golang/dep/... \

    # Cleanup

    && rm -rf /var/cache/apk/* \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*

WORKDIR $GOPATH
