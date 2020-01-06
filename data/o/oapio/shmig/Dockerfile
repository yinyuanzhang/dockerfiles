FROM alpine:latest

RUN apk update && \
    apk add bash postgresql-client mysql-client sqlite && \
    apk add --update openssl

ADD shmig /bin/shmig

CMD ["shmig"]
