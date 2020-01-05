FROM golang:latest
MAINTAINER Marshall Lee <marshall.s.lee@gmail.com>

RUN mkdir /app

ADD cmd/chitchat-session /app/cmd/chitchat-session
ADD config /app/config
ADD consts /app/consts
ADD handler /app/handler
ADD consts /app/keyset
ADD model /app/model
ADD monitoring /app/monitoring
ADD response /app/response

WORKDIR /app/cmd/chitchat-session
COPY . .

RUN go get -t github.com/gorilla/mux
RUN go get -t github.com/newrelic/go-agent
RUN go get -t gopkg.in/yaml.v2
RUN go get -t github.com/go-redis/redis
RUN go get -t github.com/tidwall/gjson
RUN go get -t github.com/valyala/fasthttp
RUN go get -t github.com/valyala/fasthttp/fasthttpadaptor
RUN go get -t github.com/google/uuid

EXPOSE 12377

RUN go build -o chitchat-session .

CMD ./chitchat-session