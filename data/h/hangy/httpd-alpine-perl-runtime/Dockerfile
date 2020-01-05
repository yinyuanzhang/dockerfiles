FROM httpd:alpine

RUN apk -U add --no-cache tzdata git curl wget perl perl-dev openssl openssl-dev make gcc libc-dev zlib-dev \
    && rm -rf /var/cache/apk/*

RUN curl -o- -L --compressed https://git.io/cpm | perl - install App::cpm -g && rm -rf ~/.perl-cpm
