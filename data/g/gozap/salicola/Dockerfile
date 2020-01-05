FROM golang:1.12.0-alpine3.9 AS builder

ENV GO111MODULE on
ENV GOPROXY https://athens.azurefd.net

RUN go get github.com/gozap/salicola \
    && go install -ldflags "-w -s" github.com/gozap/salicola

FROM alpine:3.9

LABEL maintainer="mritd <mritd1234@gmail.com>"

RUN apk upgrade --no-cache \
    && apk add ca-certificates

COPY --from=builder /go/bin/salicola /usr/bin/salicola

EXPOSE 8080

CMD ["salicola"]
