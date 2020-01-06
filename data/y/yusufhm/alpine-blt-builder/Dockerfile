FROM alpine:3.8

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://bitbucket.org/yusufhm/reins" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="0.1.0"

RUN apk add --no-cache \
      curl git nodejs-npm openssh-client patch \
      php7 php7-bcmath php7-bz2 php7-ctype php7-curl php7-dom php7-fileinfo php7-gd php7-iconv php7-json php7-mbstring php7-openssl php7-pdo php7-phar php7-session php7-simplexml php7-tokenizer php7-xml php7-xmlwriter php7-zip php7-zlib \
      python rsync

# Install composer.
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php --install-dir=bin --filename=composer && \
    rm composer-setup.php && \
    echo 'export PATH="$HOME/.composer/vendor/bin:$PATH"' >> /etc/profile && \
    composer global require hirak/prestissimo

# Install grunt, gulp and update npm.
RUN npm install -g grunt-cli gulp-cli npm
