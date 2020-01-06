FROM golang:alpine

ENV PROJECT_ROOT=/go/src/github.com/kstola2/dadbot

RUN rm -rf /var/cache/apk/* && \
    apk update && \
    apk add --no-cache git gcc musl-dev bash && \
    go get -v github.com/kstola2/dadbot/... && \
    cd ${PROJECT_ROOT} && \
    go build -o rundadbot && \
    apk del git gcc musl-dev bash

EXPOSE 80

WORKDIR ${PROJECT_ROOT}

ENTRYPOINT ["./rundadbot"]