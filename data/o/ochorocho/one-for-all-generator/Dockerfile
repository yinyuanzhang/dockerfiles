FROM alpine:3.7

# Install general stuff
RUN apk update && apk upgrade && apk --update add python python-dev py-pip build-base &&\
# Install Sphinx doc and theme
    pip install --upgrade pip && \
    pip install -U Sphinx && \
    pip install sphinx_rtd_theme && \
# Install doxygen
    apk --update add doxygen && \
# Install PHP + mods
    apk --update --no-cache --update-cache --allow-untrusted add \
    curl php7 php7-bcmath php7-json php7-mbstring php7-openssl php7-iconv php7-phar php7-curl php7-gd php7-iconv php7-mysqli php7-pdo php7-sockets php7-xml php7-exif php7-zlib php7-dom php7-tokenizer php7-xmlwriter && \
# Install Composer
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer && \
# Clean cache
    rm -rf /var/cache/apk/* && \
    apk del curl wget build-base python-dev