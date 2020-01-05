FROM golang:latest 

RUN mkdir /app 
ADD . /app/ 

WORKDIR /app 

RUN go get github.com/globalsign/mgo
RUN go get github.com/go-redis/redis
RUN go get gopkg.in/telegram-bot-api.v4
RUN go build -o main . 

CMD ["/app/main"]
