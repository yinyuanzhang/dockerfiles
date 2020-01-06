FROM golang:1.10-alpine

ENV MTAIL_VERSION "v3.0.0-rc10"

ENV GOPATH     /go
ENV SRC_PATH   /go/src/github.com/google/mtail

RUN apk add --update --no-cache --virtual build-dependencies findutils git make \
    && git clone -b $MTAIL_VERSION --single-branch https://github.com/google/mtail.git $SRC_PATH \
    && cd $SRC_PATH \
    && make \
    && mv mtail /usr/local/bin/mtail \
    && rm -rf $GOPATH \
    && apk del build-dependencies

CMD ["mtail", "--help"]