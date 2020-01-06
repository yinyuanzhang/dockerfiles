FROM golang:alpine

RUN apk add --no-cache git

# Install migrate for db migrations
RUN go get -u -d github.com/golang-migrate/migrate/cli github.com/lib/pq && \
    go build -tags 'postgres' -o /usr/local/bin/migrate github.com/golang-migrate/migrate/cli

ENTRYPOINT ["migrate"]
CMD ["--help"]
