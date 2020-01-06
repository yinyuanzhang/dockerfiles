# preparing the publish image
FROM alpine:latest as base
RUN apk add ca-certificates

# build the source
FROM golang:latest as build
WORKDIR /helloworld
COPY . .
RUN go get -v ./...
RUN CGO_ENABLED=0 GOOS=linux go build -o bin/hw cmd/app/main.go

# copy the builded file from the build container and prepare the publish image
FROM base as prod
WORKDIR /helloworld
COPY --from=build /helloworld/bin/hw hw
COPY static static
EXPOSE 8080

CMD ["./hw"]