FROM alpine:3.9

RUN apk add --update nginx curl
RUN rm -rf /var/cache/apk/* && rm -rf /tmp/*

RUN adduser -D -g 'www' www \
    && chown -R www:www /var/www

CMD ["nginx"]