# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

FROM golang:1.11.2-alpine3.8
LABEL maintainer="Fabrice Rabaute fabrice@arista.com"

RUN apk update && apk add \
    git \
    make \
    && go get github.com/jteeuwen/go-bindata/...
