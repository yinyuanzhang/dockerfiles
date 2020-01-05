#根据brook-v20181212制作 2018-12-10
FROM golang:alpine as builder
RUN apk add --update git
RUN go get github.com/txthinking/brook/cli/brook


FROM chenhw2/alpine:base
LABEL MAINTAINER Frank <https://github.com/frankpen>

# /usr/bin/brook
COPY --from=builder /go/bin /usr/bin

ENV ARGS="server -l :10300"
ENV PASSWD="password"
EXPOSE 10300/tcp 10300/udp

CMD /usr/bin/brook ${ARGS} -p ${PASSWD}
