FROM golang:1.10.5-alpine3.8

RUN apk --update add git go && mkdir  /go/pkg /go/logs 

ADD ./config/start.sh /home/

RUN chmod u+x /home/start.sh

ENV GOPATH=/go

CMD ["/home/start.sh"]