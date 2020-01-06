FROM golang:1.11.2 AS builder

ENV GO111MODULE on

# Copy the code from the host and compile it
WORKDIR /app

COPY go.mod go.sum ./

# Install global dependencies
RUN go get -u github.com/gobuffalo/packr/packr

# Download Dependencies
RUN go mod download

COPY . ./

RUN CGO_ENABLED=1 GOOS=linux packr build -o /aloud .

FROM alpine:3.7

RUN apk --update upgrade
RUN apk add sqlite
# See http://stackoverflow.com/questions/34729748/installed-go-binary-not-found-in-path-on-alpine-linux-docker
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2

# removing apk cache
RUN rm -rf /var/cache/apk/*

LABEL maintainer="spencer@spencercharest.com"
LABEL description="Aloud"

ENV ALOUD_DOCKER true

VOLUME /data

VOLUME /input

EXPOSE 4220

RUN apk --no-cache add ca-certificates

COPY --from=builder /aloud ./

ENTRYPOINT ["/aloud"]
