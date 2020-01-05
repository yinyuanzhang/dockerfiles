FROM snooxy/php7-fpm
RUN apk add --update nodejs nodejs-npm
RUN apk --update add \
        wget \
        gnupg \
    && rm -rf /var/cache/apk/*

RUN npm install -g bower grunt-cli

WORKDIR /usr/share/nginx

CMD ["bash"]
