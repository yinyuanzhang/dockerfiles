FROM hangy/httpd-alpine-perl-runtime:0.1

RUN apk add --update libxml2-dev \
    && rm -rf /var/cache/apk/*

COPY cpanfile /usr/local/apache2/cpanfile
RUN cpm install --verbose -g && rm -rf ~/.perl-cpm /usr/local/apache2/cpanfile