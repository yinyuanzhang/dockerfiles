
# build stage
FROM golang:1.11-alpine AS build-env

RUN apk add --no-cache git mercurial
RUN go get -v -u github.com/golang/dep/cmd/dep
RUN go get -v github.com/improbable-eng/grpc-web/go/grpcwebproxy ; exit 0
RUN cd src/github.com/improbable-eng/grpc-web && dep ensure
RUN go get -v -u github.com/improbable-eng/grpc-web/go/grpcwebproxy

# final stage
FROM alpine
WORKDIR /app/
COPY --from=build-env /go/bin/grpcwebproxy /app/

EXPOSE 80 443
ENTRYPOINT /app/grpcwebproxy
