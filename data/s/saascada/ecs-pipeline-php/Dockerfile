# Image Located: Dockerhub - saascada/ecs-pipeline-php
# Build: docker build -t saascada/ecs-pipeline-php .
# Push: docker push saascada/ecs-pipeline-php
FROM docker/compose:1.24.0
LABEL maintainer="developers@saescada.com"
RUN apk -Uuv --no-cache add jq git openssh-client curl php php-curl php-fileinfo php-pdo php-dom php-xsl php-gmp php-xml php-simplexml php-xmlwriter php-tokenizer php-openssl php-json php-iconv php-mbstring php-phar php-zip python py-pip rsync
RUN pip install awscli
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer
RUN apk --purge -v del py-pip curl
RUN rm /var/cache/apk/*