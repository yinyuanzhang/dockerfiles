

FROM golang:1.8

WORKDIR /go/src/cr8-data
COPY . .


RUN go get -d -v ./...
RUN go install -v ./...

CMD ["cr8-data"]
