FROM composer

RUN composer global require deployer/deployer --dev; \
    composer global require deployer/recipes --dev

ENV PATH="/tmp/vendor/bin:${PATH}"

RUN apk update
RUN apk add rsync openssh
