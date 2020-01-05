FROM golang:1.11-alpine3.8 as build
ARG PACKAGE=github.com/pagero/gocd-lifecycle
RUN mkdir -p /go/src/${PACKAGE}
WORKDIR /go/src/${PACKAGE}
COPY . .
RUN go build ./cmd/lifecycle
RUN go build ./cmd/operator

FROM alpine:3.8
ARG PACKAGE=github.com/pagero/gocd-lifecycle
RUN apk --update add ca-certificates
RUN mkdir /app
COPY --from=build /go/src/${PACKAGE}/lifecycle /app/
COPY --from=build /go/src/${PACKAGE}/operator /app/

ENTRYPOINT [ "/app/lifecycle" ]
