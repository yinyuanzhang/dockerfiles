FROM alpine:latest

WORKDIR /app

RUN apk --no-cache add \
    bash \
    bind-tools \
    ca-certificates \
    git \
    curl \
    unzip \
    php7 \
    php7-openssl \
    php7-curl \
    php7-json \
    php7-dom \
    php7-phar \
    php7-tokenizer \
    php7-iconv \
    php7-intl \
    php7-mbstring \
    php7-xml

# Download the latest phar file from Google Drive.
RUN curl -sL 'https://drive.google.com/uc?export=download&id=1ekyddD40wrUBT0GCjHo3Kh1JEL8skLqf' > /usr/local/bin/cfcli \
    && chmod +x /usr/local/bin/cfcli

COPY resources/php.ini /etc/php7/php.ini

# Install libsvm, compile from source, and then remove dependencies.
COPY resources/libsvm.sh /tmp/libsvm.sh
RUN apk add --no-cache --virtual .build-deps \
    g++ \
    make \
    && chmod +x /tmp/libsvm.sh \
    && /tmp/libsvm.sh \
    && rm /tmp/libsvm.sh \
    && apk del .build-deps

RUN cfcli setup:verify

ENTRYPOINT ["cfcli"]
