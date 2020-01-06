FROM alpine:3.7

RUN apk --no-cache add sqlite

VOLUME /src

WORKDIR /src
ENTRYPOINT ["sqlite3"]
