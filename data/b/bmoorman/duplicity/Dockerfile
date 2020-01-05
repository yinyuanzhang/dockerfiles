FROM bmoorman/alpine:3.9

RUN apk add --no-cache \
    duplicity \
    rsync

ENTRYPOINT ["duplicity"]
CMD ["--help"]
