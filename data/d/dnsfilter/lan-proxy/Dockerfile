FROM golang:1.12.5-alpine3.9

# Add/del git in one RUN to avoid bloating our image.
RUN apk update \
&& apk add --no-cache git make curl musl-dev libpcap-dev gcc \
&& curl -fsSL -o /usr/local/bin/dep https://github.com/golang/dep/releases/download/v0.5.3/dep-linux-amd64 && chmod +x /usr/local/bin/dep

ENV SRC_HOME=/go/src/github.com/DNSFilter/relay

COPY . $SRC_HOME

RUN cd $SRC_HOME \
&& dep ensure -vendor-only \
&& cd cmd/relay \
&& go build -ldflags="-s -w" -o /go/bin/relay \
&& GOOS=linux GOARCH=amd64 go build -ldflags='-s -w -linkmode external -extldflags "-static"' -o /go/bin/relay-linux-amd64 \
&& GOOS=linux GOARCH=arm go build -ldflags="-s -w" -o /go/bin/relay-linux-arm \
&& GOOS=linux GOARCH=arm64 go build -ldflags="-s -w" -o /go/bin/relay-linux-arm64 \
&& GOOS=linux GOARCH=mipsle go build -ldflags="-s -w" -o /go/bin/relay-linux-mipsle \
&& GOOS=darwin GOARCH=amd64 go build -ldflags="-s -w" -o /go/bin/relay-darwin-amd64 \
&& GOOS=windows GOARCH=amd64 go build -ldflags="-s -w" -o /go/bin/relay-windows-amd64.exe \
&& cp /go/bin/relay /go/bin/lan-proxy \
&& cp /go/bin/relay-linux-amd64 /go/bin/lan-proxy-linux-amd64 \ 
&& go install \
&& apk del git make musl-dev libpcap-dev gcc \
&& cd /go/bin \
&& rm -rf /go/src/github.com \
&& rm /usr/local/bin/dep

CMD relay
