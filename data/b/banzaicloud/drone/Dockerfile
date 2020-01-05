# docker build --rm -t banzaicloud/drone .

FROM golang:1.11-alpine as golang

RUN apk add --no-cache ca-certificates git

# For EKS cluster access the IAM authenticator is needed
RUN go get -d github.com/kubernetes-sigs/aws-iam-authenticator/cmd/aws-iam-authenticator
RUN cd $GOPATH/src/github.com/kubernetes-sigs/aws-iam-authenticator && \
    git checkout 981ecbeef8ead2720c42a62fc41d40ed6a145421 && \
    go install ./cmd/aws-iam-authenticator

ADD . /go/src/github.com/drone/drone
WORKDIR /go/src/github.com/drone/drone

RUN GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o /release/drone-server github.com/drone/drone/cmd/drone-server
RUN GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o /release/drone-agent github.com/drone/drone/cmd/drone-agent

FROM alpine:3.7
EXPOSE 8000 9000 80 443

ENV DATABASE_DRIVER=sqlite3
ENV DATABASE_CONFIG=/var/lib/drone/drone.sqlite
ENV GODEBUG=netdns=go
ENV XDG_CACHE_HOME /var/lib/drone

COPY --from=golang /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=golang /go/bin/aws-iam-authenticator /bin
COPY --from=golang /release/drone-server /bin
COPY --from=golang /release/drone-agent /bin

ENTRYPOINT ["/bin/drone-server"]
