# Build image
FROM golang:1.12.3-alpine AS builder

ENV GOFLAGS="-mod=readonly"

RUN apk add --update --no-cache ca-certificates make git curl mercurial bzr

RUN mkdir -p /workspace
WORKDIR /workspace

ARG GOPROXY

COPY go.* /workspace/
RUN go mod download

COPY . /workspace

RUN make build-release


# Final image
FROM alpine:3.9.3

RUN apk add --update --no-cache ca-certificates tzdata bash curl

COPY defaults.yaml /
COPY --from=builder /workspace/build/release/pipeline-client /usr/local/bin

ENTRYPOINT ["/usr/local/bin/pipeline-client"]
CMD ["/defaults.yaml", "session.yaml"]
