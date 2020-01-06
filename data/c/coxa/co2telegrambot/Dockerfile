FROM golang:1.13

RUN go get -d -v -u go.mongodb.org/mongo-driver/mongo github.com/go-telegram-bot-api/telegram-bot-api


COPY ./src /go/src
RUN GOOS=linux GOARM=7 go build -o /app/main /go/src/app/entry.go
WORKDIR /app
CMD ["/app/main"]
