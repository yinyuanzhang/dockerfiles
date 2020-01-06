FROM tutum/lamp:latest

ENV MYSQL_PASS Crifa@123

RUN apt-get update && apt-get -y install nano git curl php5-mcrypt php5-curl
RUN php5enmod mcrypt && php5enmod curl
RUN /usr/sbin/a2enmod rewrite
RUN /usr/bin/curl -sS https://getcomposer.org/installer |/usr/bin/php
RUN /bin/mv composer.phar /usr/local/bin/composer
RUN cd app && rm -rf * && rm -rf .git
RUN chgrp www-data /app && chmod g+s /app
RUN find /app -type d -exec chmod -R 775 {} \;
RUN find /app -type f -exec chmod -R 665 {} \;

ADD index.php /app

EXPOSE 80 3306

CMD ["/run.sh"]
