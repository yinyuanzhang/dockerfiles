FROM golang as builder
ADD . /go/src/github.com/xiaomi/naftis/
RUN cd /go/src/github.com/xiaomi/naftis/ \
  && make build.api

FROM scratch

COPY --from=builder /go/src/github.com/xiaomi/naftis/bin/naftis-api /usr/app/naftis/bin/

EXPOSE 50000

ENTRYPOINT ["/usr/app/naftis/bin/naftis-api", "start"]
