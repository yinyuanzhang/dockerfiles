FROM golang:1.13.3-alpine AS builder

# Install packages
RUN apk add --no-cache bash gcc musl-dev git linux-headers

# Compile application
WORKDIR /go/src/github.com/mysteriumnetwork/transactor
ADD . .
RUN go run mage.go -v swag
RUN go run mage.go -v build

FROM alpine:3.9

# Install packages
RUN apk add --no-cache ca-certificates

# Install application
COPY --from=builder /go/src/github.com/mysteriumnetwork/transactor/build/transactor /usr/bin/transactor

ENTRYPOINT ["/usr/bin/transactor"]
