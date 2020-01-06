FROM golang:1.10-alpine as builder

WORKDIR /go/src/github.com/monostream/luegi/
COPY . .

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o luegi .



FROM ubuntu:18.04

RUN apt-get update && apt-get install -y dumb-init tesseract-ocr-all && rm -rf /var/lib/apt/lists/*
ENV LANG C.UTF-8

WORKDIR /app/
COPY --from=builder /go/src/github.com/monostream/luegi/luegi .

ENV PATH "/app:${PATH}"

ENV PORT=8080
ENV GIN_MODE=release

EXPOSE 8080

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["luegi"]

