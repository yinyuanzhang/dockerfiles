# Copyright (c) 2019 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.


FROM golang:1.11.4-alpine3.8 as build
LABEL maintainer="Fabrice Rabaute fabrice@arista.com"

ENV VERSION 1.2.0

RUN apk add git make bash \
  && go get -u github.com/golang/dep/cmd/dep \
  && mkdir -p /go/src/github.com/bloomberg \
  && cd /go/src/github.com/bloomberg \
  && wget -O goldpinger.tar.gz https://github.com/bloomberg/goldpinger/archive/${VERSION}.tar.gz \
  && tar xvf goldpinger.tar.gz \
  && mv goldpinger-${VERSION} goldpinger \
  && cd goldpinger \
  && make vendor \
  && make bin/goldpinger

FROM aristanetworks/base:2.3
LABEL maintainer="Fabrice Rabaute fabrice@arista.com"

COPY --from=build /go/src/github.com/bloomberg/goldpinger/bin/goldpinger /goldpinger

COPY --from=build /go/src/github.com/bloomberg/goldpinger/static /static

ENTRYPOINT ["/usr/bin/dumb-init", "--", "/goldpinger"]
