FROM golang:1.12.5-alpine as builder
LABEL maintainer="Eden Cadagiani <e.cadagiani@gmail.com>"
# FORK OF SISH: maintainer="Antonio Mika <e.cadagiani@gmail.com>"

RUN apk add --no-cache git gcc musl-dev

ENV GOCACHE /gocache

WORKDIR /usr/local/go/src/github.com/antoniomika/sish

COPY go.mod .
COPY go.sum .

RUN go mod download

COPY . .

RUN go install
RUN go test -i ./...

FROM alpine
LABEL maintainer="Eden Cadagiani <e.cadagiani@gmail.com>"
# FORK OF SISH: maintainer="Antonio Mika <e.cadagiani@gmail.com>"

COPY --from=builder /usr/local/go/src/github.com/antoniomika/sish /sish
COPY --from=builder /go/bin/sish /sish/sish

WORKDIR /sish

ENTRYPOINT ["/sish/sish"]
