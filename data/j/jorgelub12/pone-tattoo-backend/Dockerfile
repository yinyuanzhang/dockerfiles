FROM golang:1.10

WORKDIR /go/src/bitbucket.org/jorgelub12/ponetattoo-backend
COPY . .

RUN go get -d -v ./...
RUN go get -u github.com/golang/protobuf/proto
RUN go get -u github.com/golang/protobuf/protoc-gen-go
RUN go build

EXPOSE 8082
CMD ["./ponetattoo-backend"]
