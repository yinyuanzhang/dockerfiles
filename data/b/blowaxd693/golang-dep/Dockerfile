# This file is a template, and might need editing before it works on your project.
FROM golang:1.11-alpine AS builder

LABEL maintainer="BlowaXD <blowa@noswings.com>"

RUN apk add --no-cache git \
	&& go get -u github.com/golang/dep/cmd/dep

RUN go build $GOPATH/src/github.com/golang/dep/cmd/dep && mv $GOPATH/bin/dep /bin/dep

FROM golang:1.11-alpine

COPY --from=builder /bin/dep /bin/dep

# We'll likely need to add SSL root certificates
RUN chmod +x /bin/dep && apk --no-cache add ca-certificates

CMD ["dep"]