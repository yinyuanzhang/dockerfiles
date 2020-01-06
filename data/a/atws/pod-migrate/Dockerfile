FROM alpine
ADD entrypoint.sh /entrypoint.sh
RUN apk --no-cache add wget openssl curl rsync mysql-client ca-certificates
ENTRYPOINT ["/entrypoint.sh"]
