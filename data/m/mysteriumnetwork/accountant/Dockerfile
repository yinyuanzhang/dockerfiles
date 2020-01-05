FROM golang:1.13-alpine AS builder

# Install packages
RUN apk add --no-cache bash gcc musl-dev git curl linux-headers

# Compile application
WORKDIR /go/src/github.com/mysteriumnetwork/accountant
ADD . .
RUN go run mage.go -v swag
RUN go run mage.go -v build

FROM alpine:latest

# Install packages
RUN apk add --no-cache ca-certificates

# Install application
COPY --from=builder /go/src/github.com/mysteriumnetwork/accountant/build/accountant /usr/bin/accountant

ENTRYPOINT ["/usr/bin/accountant"]
