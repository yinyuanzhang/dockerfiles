FROM golang:1.8 as builder
LABEL maintainer="Maarten van der Hoef <maarten@doingcloudright.com>"

WORKDIR /go/src/app

COPY . .

RUN go get -d -v ./...
RUN make bin/assume-role


# Stage 2
FROM alpine:latest as runner

RUN apk --no-cache add ca-certificates
WORKDIR /usr/local/bin

RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2

# copy the binary from previous stage
COPY --from=builder /go/src/app/bin/assume-role .

# execute
ENTRYPOINT ["/usr/local/bin/assume-role"]
