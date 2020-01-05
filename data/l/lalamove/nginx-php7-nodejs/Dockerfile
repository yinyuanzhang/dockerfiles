FROM lalamove/nginx-php7:alpine-1.0.8

RUN \
    apk --no-cache add --update nodejs-npm && \
    rm -rf /var/cache/apk/* && \
    npm install -g yarn

CMD ["/entry.sh"]
