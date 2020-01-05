FROM golang:1.12.0 as builder

RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN CGO_ENABLED=0 GOOS=linux go build -o fritz-exporter .

FROM alpine
RUN apk --update add ca-certificates
RUN mkdir /app
WORKDIR /app
COPY --from=builder /app/fritz-exporter /bin/fritz-exporter

EXPOSE 9103
ENTRYPOINT ["/bin/fritz-exporter"]
