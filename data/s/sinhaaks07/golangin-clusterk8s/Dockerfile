FROM golang:latest


WORKDIR /go/src/app
COPY . .
RUN chmod +x ./entrypoint.sh
RUN go build main.go

ENTRYPOINT ["./entrypoint.sh"]


