FROM designmynight/dockerfiles:php7.1-cli-alpine

WORKDIR /opt

RUN pear install PHP_CodeSniffer

ENTRYPOINT [ "phpcs" ]
