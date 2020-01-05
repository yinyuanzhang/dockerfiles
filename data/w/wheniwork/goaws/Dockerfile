FROM golang:1.9 as builder

WORKDIR /go/src/github.com/p4tin/goaws

RUN curl -fsSL -o /usr/local/bin/dep https://github.com/golang/dep/releases/download/v0.4.1/dep-linux-amd64 && chmod +x /usr/local/bin/dep

COPY Gopkg.lock Gopkg.toml app ./
RUN dep ensure
COPY . .

RUN CGO_ENABLED=0 go build -o goaws_linux_amd64 app/cmd/goaws.go

FROM alpine:3.7

EXPOSE 4100

COPY --from=builder /go/src/github.com/p4tin/goaws/goaws_linux_amd64 /
COPY ./app/conf/goaws.yaml /conf/
ENTRYPOINT ["/goaws_linux_amd64"]
