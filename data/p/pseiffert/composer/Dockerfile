FROM pseiffert/php-cli
MAINTAINER Paul Seiffert <paul.seiffert@gmail.com>

ENV COMPOSER_HOME /root/composer
RUN apt-get update && apt-get install -y curl git-core && apt-get clean
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

ENTRYPOINT ["composer", "--ansi"]
CMD ["--"]
