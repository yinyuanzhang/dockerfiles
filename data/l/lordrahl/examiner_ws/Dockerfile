# FROM golang:latest as build-env
FROM golang:alpine AS build-env

RUN apk --no-cache add build-base git bzr mercurial gcc

WORKDIR $GOPATH/src/github.com/LordRahl90/examiner

COPY . .
RUN go get -d -v ./...
RUN go install -v ./...
RUN go build -o examiner .

# RUN ls -al



FROM alpine
COPY --from=build-env /go/src/github.com/LordRahl90/examiner ./

EXPOSE 5600

# RUN ls -al

CMD ["./examiner"]