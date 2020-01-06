FROM golang:1.10.3-alpine3.7 as builder

WORKDIR /go/src/bamboomq.tech/bamboomq
COPY . .

RUN go install -ldflags "-s -w" -tags netgo bamboomq.tech/bamboomq/cmd/...


FROM alpine:3.7

COPY --from=builder /go/bin/* /usr/local/bin/

CMD ["bamboomq"]
