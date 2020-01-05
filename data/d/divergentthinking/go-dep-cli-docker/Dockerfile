FROM golang:1.12.5-alpine3.9

RUN apk add --no-cache git \ 
    && go get -u github.com/golang/dep/cmd/dep

WORKDIR /go

ADD dep.sh .

ENTRYPOINT ["sh", "dep.sh"]