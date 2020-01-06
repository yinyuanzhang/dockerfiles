FROM golang:1.9-alpine
MAINTAINER Ali Al-Shabibi <ali@cerra.io>

VOLUME /go/src
RUN apk --update add git curl gettext

WORKDIR /go
RUN go get -u golang.org/x/lint/golint

COPY golint-entry-point /golint-entry-point
COPY status /status
RUN chmod 755 /golint-entry-point
ENTRYPOINT [ "/golint-entry-point" ]
