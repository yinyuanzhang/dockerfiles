FROM golang:alpine

# install git
RUN apk add --update --no-cache git curl

# install dep
RUN curl -fsSL -o /usr/local/bin/dep https://github.com/golang/dep/releases/download/v0.5.0/dep-linux-amd64 && chmod +x /usr/local/bin/dep

RUN mkdir -p /go/src/github.com/matthewnitschke/dash-apis
WORKDIR /go/src/github.com/matthewnitschke/dash-apis

COPY . /go/src/github.com/matthewnitschke/dash-apis

RUN dep ensure -vendor-only

CMD ["go", "run", "/go/src/github.com/matthewnitschke/dash-apis/main.go"]