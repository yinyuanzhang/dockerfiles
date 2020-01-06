FROM golang:latest
MAINTAINER Marshall Lee <marshall.s.lee@gmail.com>

RUN mkdir /app

ADD cmd/chitchat-users /app/cmd/chitchat-users
ADD config /app/config
ADD consts /app/consts
ADD db /app/db
ADD errorcheck /app/errorcheck
ADD handler /app/handler
ADD model /app/model
ADD app /app/app
ADD response /app/response
ADD security /app/security
ADD session /app/session

WORKDIR /app/cmd/chitchat-users
COPY . .

RUN go get -t github.com/jinzhu/gorm
RUN go get -t github.com/gorilla/mux
RUN go get -t github.com/newrelic/go-agent
RUN go get -t gopkg.in/yaml.v2
RUN go get -t github.com/go-sql-driver/mysql
RUN go get -t github.com/valyala/fasthttp
RUN go get -t github.com/tidwall/gjson

EXPOSE 12374

RUN go build -o chitchat-users .

CMD ./chitchat-users