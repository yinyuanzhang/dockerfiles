FROM alpine

RUN apk add --update openssl && \
rm -rf /var/cache/apk/*

COPY script.sh /script/script.sh

RUN chmod +x /script/script.sh

CMD ["./script/script.sh"]
