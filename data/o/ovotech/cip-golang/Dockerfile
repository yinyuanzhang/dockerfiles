FROM golang:1.12-alpine

RUN apk --no-cache --update add \
    build-base \
    ca-certificates \
    git \
    openssh
    
RUN git config --global url."git@github.com:ovotech/".insteadOf "https://github.com/ovotech/"

RUN GO111MODULE=on go get -u github.com/golangci/golangci-lint/cmd/golangci-lint@v1.17.1
RUN GO111MODULE=on go get -u honnef.co/go/tools/cmd/staticcheck@2019.2.1
RUN go get -u github.com/jstemmer/go-junit-report
