# Base image is in https://registry.hub.docker.com/_/golang/
# CREATE hello: sudo docker run --rm -v "$(pwd)":/go/src/ -w /go/src jojo13572001/shopgame bee new hello
# RUN hello:  sudo docker run --rm -v "$(pwd)"/hello:/go/src/hello -w /go/src/hello -p 8081:8080 jojo1357201/shopgame

FROM jojo13572001/shopgame
MAINTAINER Wright Yen jojo13572001@yahoo.com.tw

# ENV GOPATH /go

# Install beego & bee
RUN go get github.com/astaxie/beego
RUN go get github.com/beego/bee
