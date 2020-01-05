FROM golang:1.12 as builder
WORKDIR /go/src/app
COPY ./main.go main.go
COPY ./auth.go auth.go
COPY ./calendar.go calendar.go
COPY ./google_utils.go google_utils.go
COPY ./tasks.go tasks.go
COPY ./entrypoint.sh /opt/entrypoint.sh

RUN go get -d -v ./... && \
    CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /opt/app . && \
    chmod +x /opt/entrypoint.sh

FROM alpine

RUN apk --no-cache add ca-certificates

WORKDIR /app
COPY --from=builder /opt .
COPY ./credentials.json.dummy credentials.json
COPY ./token.json.dummy token.json

ENTRYPOINT ["./entrypoint.sh"]
CMD ["./app"]