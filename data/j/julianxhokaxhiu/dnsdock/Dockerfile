# This file is part of DNSDock
# MIT
#
# Copyright (C) 2014 Tõnis Tiigi <tonistiigi@gmail.com>
# Copyright (C) 2017 Julian Xhokaxhiu <info@julianxhokaxhiu.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# build image
FROM golang:alpine

ENV CGO_ENABLED=0
ENV GOARCH=amd64

RUN apk update && apk add git
RUN go get -v github.com/tools/godep
RUN go get -u github.com/golang/lint/golint
RUN go get github.com/ahmetb/govvv

RUN mkdir -p /go/src/github.com/aacebedo/dnsdock
WORKDIR /go/src/github.com/aacebedo/dnsdock
ADD . /go/src/github.com/aacebedo/dnsdock

RUN mkdir /tmp/output
RUN godep restore
WORKDIR /go/src/github.com/aacebedo/dnsdock/src

RUN govvv build -o /tmp/output/dnsdock
RUN golint -set_exit_status

# AMD64
RUN go vet
RUN go test ./...

# -----------------

# run image
FROM alpine
COPY --from=0 /tmp/output/dnsdock /bin/dnsdock
ENTRYPOINT ["dnsdock"]
