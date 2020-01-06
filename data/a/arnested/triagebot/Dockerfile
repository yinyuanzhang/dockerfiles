FROM golang:1.13.5-alpine AS build-env

WORKDIR /build

ENV GO111MODULE=on
ENV CGO_ENABLED=0
ENV GOOS=linux

RUN apk --no-cache add git=~2

COPY *.go go.mod go.sum /build/

RUN go version
RUN go build
RUN go test -o ./triagebot.test -v -cover ./...

FROM scratch

ENV PATH=/

COPY --from=build-env /usr/local/go/lib/time/zoneinfo.zip /usr/local/go/lib/time/zoneinfo.zip
COPY --from=build-env /etc/ssl/certs/ /etc/ssl/certs/
COPY --from=build-env /build/triagebot /triagebot
COPY --from=build-env /build/triagebot.test /test

ENTRYPOINT ["triagebot"]
