FROM golang:1.11.2 as builder
WORKDIR /go/src/github.com/rira12621/go-word-counter/
COPY main.go .
# only one OS for now, could be templated
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o go-word-counter .

# app doesn't do much so use minimal image
FROM alpine:latest
WORKDIR /root/
# add testfile from repo
ADD testfiles/testfile .
# copy binary from builder stage
COPY --from=builder /go/src/github.com/rira12621/go-word-counter/go-word-counter .
CMD ["./go-word-counter","testfile"]
