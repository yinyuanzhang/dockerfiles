# Build image
FROM golang:1.11.5 AS build-env
WORKDIR /root/
COPY . ./
RUN CGO_ENABLED=0 GOOS=linux go build -a

# Runtime image
FROM alpine:3.9
WORKDIR /root/
COPY --from=build-env /root/reddit-filters ./
COPY assets ./assets
COPY templates ./templates
RUN apk update && apk add ca-certificates
EXPOSE 8080
CMD ["./reddit-filters"]
