
FROM golang:alpine as builder
RUN apk --no-cache add ca-certificates && apk update && apk add --no-cache git
RUN mkdir /build
ADD . /build/
WORKDIR /build
RUN go get -d -v ./...
RUN GOOS=linux GOARCH=386 go build -o worker

FROM scratch
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /build/worker /app/
EXPOSE 8200
CMD ["/app/worker"]

