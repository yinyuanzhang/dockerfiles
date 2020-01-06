FROM golang:alpine

WORKDIR /go/src/app

RUN mkdir /watch
RUN mkdir /queue
RUN apk update; apk add --no-cache git
RUN go get github.com/alexellis/jaas
RUN go install github.com/alexellis/jaas

COPY ./myapp/ .

RUN go get -d ./...
RUN go install ./...

CMD ["app"]
