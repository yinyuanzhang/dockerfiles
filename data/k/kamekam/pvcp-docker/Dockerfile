FROM alpine:latest
LABEL maintener="Cam Yilmaz <yilmaz.cam@groupepvcp.com>"
LABEL description="Test for Apache container"
ENV PHPVERSION 7
RUN apk add --update apache2 php${PHPVERSION}-apache2 php${PHPVERSION} && \
        rm -rf /var/cache/apk/* && \
        rm -rf /var/www/localhost/htdocs/index.html && \
        echo "<?php phpinfo(); ?>" > /var/www/localhost/htdocs/index.php && \
        chmod 755 /var/www/localhost/htdocs/index.php && \
        echo "<htm> <body> <h1> TITI </h1> </body> </html>" >> /var/www/localhost/htdocs/index.php
EXPOSE 80/tcp
ENTRYPOINT ["httpd"]
CMD ["-D", "FOREGROUND"]
