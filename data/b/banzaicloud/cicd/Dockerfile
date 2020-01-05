# docker build --rm -t banzaicloud/cicd .

FROM golang:1.12-alpine as golang

RUN apk add --no-cache ca-certificates git

# For EKS cluster access the IAM authenticator is needed
RUN go get -d github.com/kubernetes-sigs/aws-iam-authenticator/cmd/aws-iam-authenticator
RUN cd $GOPATH/src/github.com/kubernetes-sigs/aws-iam-authenticator && \
    git checkout 981ecbeef8ead2720c42a62fc41d40ed6a145421 && \
    go install ./cmd/aws-iam-authenticator

ADD . /go/src/github.com/banzaicloud/cicd
WORKDIR /go/src/github.com/banzaicloud/cicd

RUN GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o /release/cicd-server github.com/banzaicloud/cicd/cmd/cicd-server
RUN GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o /release/cicd-agent github.com/banzaicloud/cicd/cmd/cicd-agent

FROM alpine:3.7
EXPOSE 8000 9000 80 443

ENV DATABASE_DRIVER=sqlite3
ENV DATABASE_CONFIG=/var/lib/cicd/cicd.sqlite
ENV GODEBUG=netdns=go
ENV XDG_CACHE_HOME /var/lib/cicd

COPY --from=golang /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=golang /go/bin/aws-iam-authenticator /bin
COPY --from=golang /release/cicd-server /bin
COPY --from=golang /release/cicd-agent /bin

ENTRYPOINT ["/bin/cicd-server"]
