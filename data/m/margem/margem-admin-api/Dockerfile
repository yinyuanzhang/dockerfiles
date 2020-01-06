FROM golang:1.13

WORKDIR $GOPATH/src/MARGEM

COPY . .

RUN go get -u github.com/golang/dep/...

RUN dep ensure

RUN go install -a -tags 'admin' -ldflags '-w -extldflags "-static"'

EXPOSE 5001

CMD ["MARGEM"]