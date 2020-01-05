FROM golang:1.10-alpine

RUN apk add --update git perl build-base bash && \
    git clone https://github.com/kdlucas/byte-unixbench.git /app && \
    go get -v github.com/yudai/gotty

WORKDIR /app/UnixBench
EXPOSE 8080

CMD gotty -w bash
