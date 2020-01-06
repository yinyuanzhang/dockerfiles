FROM golang:1.13-alpine as builder

WORKDIR /app
COPY ./ ./

RUN set -x \
 && go mod download \
 && CGO_ENABLED=0 \
    GOOS=linux \
    go build -a -v \
        -ldflags "-s -w" \
        -o do .

###############################################################################
# create actual image
###############################################################################
FROM alpine:latest
COPY --from=builder /app .
ENTRYPOINT ["./do"]
