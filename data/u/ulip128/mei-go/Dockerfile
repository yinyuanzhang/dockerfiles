# build stage
FROM golang:1.12.5-alpine3.9 as builder

ADD . /src
RUN apk add --no-cache git
RUN cd /src && go mod download && GO111MODULE=on go build -o app

# final stage
FROM alpine:3.9

WORKDIR /app
COPY --from=builder /src/app /app/
CMD ["./app"]
