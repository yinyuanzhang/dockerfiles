# build stage
FROM golang:alpine AS build-env
RUN apk add --no-cache git
COPY . /go/src/github.com/beckxie/mysql-metrics-collector
RUN cd /go/src/github.com/beckxie/mysql-metrics-collector && go build -mod=vendor

# final stage
FROM alpine
WORKDIR /mysql-metrics-collector
RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*
COPY --from=build-env /go/src/github.com/beckxie/mysql-metrics-collector /mysql-metrics-collector/
CMD ./mysql-metrics-collector