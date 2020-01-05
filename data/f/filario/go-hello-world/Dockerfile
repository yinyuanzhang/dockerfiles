FROM alpine:latest as base
RUN apk add ca-certificates

FROM golang:latest as build
WORKDIR /helloworld
COPY . .
RUN go get -v ./...
RUN CGO_ENABLED=0 GOOS=linux go build -o bin/hw cmd/app/main.go

FROM base as prod
WORKDIR /helloworld
COPY --from=build /helloworld/bin/hw hw
COPY static static
EXPOSE 8080

CMD ["./hw"]
