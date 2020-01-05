FROM golang:1.10-alpine as builder
MAINTAINER storj
RUN mkdir -p /go/src/github.com/storj/updatekate

# Add all source code
ADD . /go/src/github.com/storj/updatekate
WORKDIR /go/src/github.com/storj/updatekate
RUN apk -U add curl git
RUN curl https://glide.sh/get | sh
RUN glide install
# Run the Go installer
RUN go install -v github.com/storj/updatekate

# Start over with a fresh image
FROM alpine
# Copy in the binary from the previous stage
COPY --from=builder /go/bin/updatekate /updatekate
# Indicate the binary as our entrypoint
ENTRYPOINT /updatekate

# Expose your port
EXPOSE 8888
