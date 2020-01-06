FROM php:7.2-alpine

ENV DEPLOYER_VERSION=6.4.3

RUN apk update --no-cache \
    && apk add --no-cache \
        openssh-client
RUN apk add --update bash && rm -rf /var/cache/apk/*

RUN curl -L https://deployer.org/releases/v$DEPLOYER_VERSION/deployer.phar > /usr/local/bin/deployer \
    && chmod +x /usr/local/bin/deployer


COPY ssh-env-config.sh /usr/local/bin/ssh-env-config.sh
RUN chmod +x /usr/local/bin/ssh-env-config.sh

VOLUME ["/project"]
WORKDIR /project

ENTRYPOINT ["ssh-env-config.sh", "deployer"]
