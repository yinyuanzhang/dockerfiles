FROM golang:1.11

COPY . /go/src/gitlab.com/kodionse/cloudify

WORKDIR /go/src/gitlab.com/kodionse/cloudify

RUN go get github.com/gin-gonic/gin

RUN go build main.go

CMD ["./main"]