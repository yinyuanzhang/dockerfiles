FROM alpine:3.4
RUN apk add --update sqlite

ADD backup.sh /backup.sh
RUN chmod +x /backup.sh

VOLUME /db

ENTRYPOINT ["/backup.sh"]
CMD [""]
