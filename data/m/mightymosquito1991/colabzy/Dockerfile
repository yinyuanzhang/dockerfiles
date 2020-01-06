FROM golang:1.11 as build

WORKDIR /go/src/colabzy_backend

COPY . .

RUN go get -d ./... && go build -o _colabzy_
RUN mv _colabzy_ /usr/local/bin

EXPOSE 8100

CMD ["/bin/sh", "-c", "_colabzy_ > colabzy.log 2>&1"]
