FROM golang:1.10

WORKDIR /go/src/bitbucket.org/loopideas/beeper-school-backend
COPY . . 

# RUN go get -u -d
# RUN go get -d -v ./...
RUN go get -v
RUN go get -u github.com/golang/protobuf/proto 
RUN go get -u github.com/golang/protobuf/protoc-gen-go 
RUN go build 

EXPOSE 8082
CMD ["./beeper-school-backend"]