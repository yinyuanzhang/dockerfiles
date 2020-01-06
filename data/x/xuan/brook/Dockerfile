FROM golang:alpine as builder
RUN apk add --update git
RUN go get github.com/txthinking/brook/cli/brook


FROM chenhw2/alpine:base
LABEL MAINTAINER xuan

# /usr/bin/brook
COPY --from=builder /go/bin /usr/bin

USER nobody
ENV ARGS="server -l :6677 -p abc666"
EXPOSE 6677/tcp 6677/udp

CMD /usr/bin/brook ${ARGS}