FROM golang:latest AS builder

ADD https://github.com/golang/dep/releases/download/v0.4.1/dep-linux-amd64 /usr/bin/dep
RUN chmod +x /usr/bin/dep
RUN go get github.com/rakyll/statik

WORKDIR $GOPATH/src/gitlab.com/echocat/caretakerd.echocat.org/
COPY . ./
RUN statik -f -src=static -p=blobs
RUN dep ensure --vendor-only
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix nocgo -o /app .

FROM scratch
COPY --from=builder /app /app
ENTRYPOINT ["/app"]
