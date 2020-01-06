FROM inventis/php:7.1

LABEL maintainer="Inventis <developers@inventis.be>"

# Install composer
RUN curl https://getcomposer.org/composer.phar -o /usr/local/bin/composer && chmod +x /usr/local/bin/composer

ENV COMPOSER_ALLOW_SUPERUSER 1

RUN apt-get update && apt-get install -y ssh openssh-client git

RUN mkdir -p ~/.ssh/
RUN touch ~/.ssh/known_hosts
COPY known-host-domains /known-host-domains
RUN while read in; do ssh-keyscan -H "$in" >> ~/.ssh/known_hosts; done < /known-host-domains

COPY docker-entrypoint /usr/local/bin/
ENTRYPOINT ["docker-entrypoint"]

CMD ["composer"]
