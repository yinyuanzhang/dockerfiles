FROM golang:alpine as build-env

RUN apk update
RUN apk add alpine-sdk

WORKDIR /go/src/getswift/query-blocking
COPY get.sh /go/src/getswift/query-blocking
RUN sh get.sh

ADD . /go/src/getswift/query-blocking

RUN go install .

FROM alpine:3.6
RUN apk update
WORKDIR /app
ENV PATH "$PATH:/app"
COPY --from=build-env /go/bin/ .
