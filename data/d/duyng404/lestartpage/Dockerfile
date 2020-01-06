FROM golang:latest

WORKDIR /go/src/lestartpage
COPY . .

RUN go get -d -v ./...
RUN go install -v ./...

ENTRYPOINT ["lestartpage"]