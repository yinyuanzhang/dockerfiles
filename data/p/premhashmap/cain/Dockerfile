FROM premhashmap/cain-buildenv:latest as builder
RUN mkdir -p $GOPATH/src/github.com/prem0132 && cd $GOPATH/src/github.com/prem0132 \
    && git clone https://github.com/prem0132/cain.git && cd cain \
    && git checkout cain-incremental-backup \
    && dep ensure \
    && make build

FROM alpine:3.8
RUN apk --no-cache add ca-certificates
COPY --from=builder /go/src/github.com/prem0132/cain/bin/cain /usr/local/bin/cain
RUN addgroup -g 1001 -S cain \
    && adduser -u 1001 -D -S -G cain cain
USER cain
WORKDIR /home/cain
CMD ["cain"]

