# Build in a stock Go builder container
FROM golang:1.11-alpine as builder

RUN apk add --no-cache make gcc musl-dev linux-headers

ADD . /go-naka

ARG GIT_BRANCH=master
RUN cd /go-naka \
    && echo "Branch: ${GIT_BRANCH}" \
    && make geth git-branch=${GIT_BRANCH}

# Pull Geth into a second stage deploy alpine container
FROM alpine:latest

RUN apk add --no-cache ca-certificates
COPY --from=builder /go-naka/build/bin/geth /usr/local/bin/

EXPOSE 8545 8546 30303 30303/udp
ENTRYPOINT ["geth"]
