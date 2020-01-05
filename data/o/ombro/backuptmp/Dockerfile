FROM alpine:3.7

RUN apk update && apk add tar

WORKDIR /tmp

CMD ["sh", "-c", "tar -cvjSf /mnt/backup.tar.bz2 *"]
