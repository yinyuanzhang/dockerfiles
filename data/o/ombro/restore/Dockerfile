FROM alpine:3.7

RUN apk update && apk add tar

CMD ["sh", "-c", "rm -rf /mnt/*/** && tar -xjvf /mnt/backup.tar.bz2 -C /mnt"]
