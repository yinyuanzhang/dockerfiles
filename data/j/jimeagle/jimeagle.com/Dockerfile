# Build image
FROM golang:1.12-alpine AS build-env
WORKDIR /root/
COPY ./ ./
RUN apk update && apk add git
RUN go mod tidy && GO111MODULE=on CGO_ENABLED=0 GOOS=linux go build -a

# Runtime image
FROM alpine:3.10 AS runtime-env
WORKDIR /root/
COPY --from=build-env /root/jimeagle ./
COPY assets ./assets
COPY templates ./templates
RUN apk update && apk add ca-certificates curl bash
CMD ["./jimeagle"]
