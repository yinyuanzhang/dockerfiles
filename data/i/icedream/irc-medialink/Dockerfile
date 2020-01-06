FROM golang:1.12-alpine AS builder

RUN apk add --no-cache \
	git

ENV CGO_ENABLED 0

WORKDIR /usr/src/medialink
COPY . .
RUN go build -ldflags '-extldflags "-static"' -o /irc-medialink
RUN cp *.tpl /

###

FROM alpine:3.10

RUN apk add --no-cache ca-certificates

WORKDIR /app

COPY --from=builder /irc-medialink /usr/local/bin
COPY --from=builder /*.tpl .
ENTRYPOINT ["irc-medialink"]
