FROM golang as builder
WORKDIR /go/src/nirvana-cms
COPY . .
RUN go get
RUN CGO_ENABLED=0 GOOS=linux go build -a -v -o nirvana-cms .

FROM alpine:latest
VOLUME ["/root/config","/root/log"]
WORKDIR /root/
EXPOSE 80
COPY --from=builder /go/src/nirvana-cms/nirvana-cms .
COPY --from=builder /go/src/nirvana-cms/zoneinfo.zip /usr/local/go/lib/time/zoneinfo.zip
CMD ["/bin/sh","-c","./nirvana-cms >> log/nirvana-cms.log 2>&1"]