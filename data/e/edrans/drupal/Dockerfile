FROM edrans/apache

RUN yum install mariadb php-mysql php-xml php-gd php-drush-drush -y && yum clean all -y
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html
ADD drupal/ /app

ADD settings.php /app/sites/default/settings.php
RUN mkdir -p /app/sites/default/files
RUN chown apache:apache /app -R

ADD site-default.conf /etc/httpd/conf.d/default.conf

ADD run-drupal.sh /run-drupal.sh

EXPOSE 80

ENTRYPOINT ["/run-drupal.sh"]
CMD ["apachectl", "-D", "FOREGROUND"]
