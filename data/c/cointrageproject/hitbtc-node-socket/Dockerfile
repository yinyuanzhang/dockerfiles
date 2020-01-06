FROM golang:latest 

RUN mkdir /app 
ADD . /app/ 

WORKDIR /app 

RUN go get github.com/globalsign/mgo
RUN go get github.com/gorilla/websocket
RUN go get github.com/cointrage/orderbook-socket/orderbook
RUN go get github.com/gogo/protobuf/io
RUN go get github.com/golang/protobuf/proto

RUN go build -o main . 

CMD ["/app/main"]
