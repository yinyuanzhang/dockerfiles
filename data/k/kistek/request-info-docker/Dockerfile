FROM golang:1.10-alpine


COPY main.go /go/src/github.com/kistek/request-info-docker/

RUN cd /go/src/github.com/kistek/request-info-docker && \
    go get && \
    CGO_ENABLED=0 GOOS=linux go build -a -o /go/bin/app main.go


FROM scratch

CMD ["/app"]
COPY --from=0 /go/bin/app /app
