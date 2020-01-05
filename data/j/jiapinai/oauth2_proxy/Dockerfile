FROM golang:1.7-alpine
MAINTAINER colin.hom@coreos.com

RUN apk add --no-cache git
RUN go get github.com/tools/godep
RUN go get github.com/weppos/publicsuffix-go/publicsuffix

ADD . $GOPATH/src/github.com/bitly/oauth2_proxy

WORKDIR $GOPATH/src/github.com/bitly/oauth2_proxy

RUN godep go install github.com/bitly/oauth2_proxy

ENTRYPOINT ["oauth2_proxy"]
