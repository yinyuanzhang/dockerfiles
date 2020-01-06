FROM golang:alpine
RUN apk update && apk upgrade && \
apk add --no-cache bash git openssh && \
go get github.com/rakyll/hey
ENTRYPOINT ["hey"]
