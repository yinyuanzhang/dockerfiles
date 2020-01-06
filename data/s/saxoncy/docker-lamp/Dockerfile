FROM alpine:latest
LABEL maintainer="Yi Cheng <saxoncy@gmail.com>"
LABEL description="Example docker file to install PHP and Apache."

ENV PHPVERSION=5

RUN apk add --update apache2 php${PHPVERSION}-apache2 php${PHPVERSION} && \
    rm -rf /var/cache/apk/* && \
    mkdir /run/apache2/ && \
    rm -rf /var/www/localhost/htdocs/index.html && \
    echo "<?php phpinfo(); ?>" > /var/www/localhost/htdocs/index.php && \
    chmod 755 /var/www/localhost/htdocs/index.php

EXPOSE 80/tcp

ENTRYPOINT [ "httpd" ]
CMD [ "-D", "FOREGROUND" ]
