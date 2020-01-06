FROM golang:1.8 as builder

WORKDIR /go/src/github.com/julu/leiyunApi/
COPY . .
RUN go build -o app .
EXPOSE 8688
CMD ["./app"]

