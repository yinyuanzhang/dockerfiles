FROM golang:alpine as builder
RUN mkdir /build 
ADD . /build/
WORKDIR /build 
RUN apk add --no-cache git
RUN go get github.com/gorilla/websocket
RUN go get github.com/shirou/w32
RUN go get github.com/araujobsd/bhyve-vm-goagent/plugins
RUN go get github.com/araujobsd/bhyve-vm-goagent/termios
RUN go get github.com/araujobsd/bhyve-vm-goagent/websocket
RUN go get github.com/go-ole/go-ole
RUN go get github.com/go-ole/go-ole/oleutil
RUN go build -o bhyve-vm-goagent-linux-amd64 .
RUN go build -o goserial ./tools/host/goserial.go
FROM alpine
RUN adduser -S -D -H -h /app bhyve-guest
USER bhyve-guest
COPY --from=builder /build/bhyve-vm-goagent-linux-amd64 /app/
WORKDIR /app
CMD ["./bhyve-vm-goagent-linux-amd64 -websocket -ipaddr='0.0.0.0' -port=9191"]
