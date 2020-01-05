FROM doneproperly/php-composer-node-npm
MAINTAINER Get IT Done Properly <docker@doneproperly.xyz>

RUN apt-get update && apt-get install -y \
    calibre \
 && rm -rf /var/lib/apt/lists/*

RUN npm -g install gitbook-cli

WORKDIR /code

ENTRYPOINT ["gitbook"]
EXPOSE 4000
