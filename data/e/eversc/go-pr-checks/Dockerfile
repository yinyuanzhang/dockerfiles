FROM golang:alpine

RUN apk --no-cache add git openssh gcc musl-dev

RUN go get github.com/fzipp/gocyclo
RUN go get github.com/golang/lint/golint