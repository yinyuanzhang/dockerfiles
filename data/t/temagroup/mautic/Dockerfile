FROM wordpress

COPY tema-entrypoint.sh /usr/local/bin/
COPY .htaccess /var/www/html/.htaccess-optimized
RUN chown www-data:www-data /var/www/html/.htaccess-optimized

RUN \
  apt-get update; \
  apt-get install -y unzip vim

COPY php-upload.ini /usr/local/etc/php/conf.d

# we need to remove latest line from standard docker-entrypoint.sh
# and add to our custom entrypoint. With this, we can add new commands
# before start the apache server :)
RUN \
  COMMAND=$(tail -n 1 /usr/local/bin/docker-entrypoint.sh); \
  sed '$d' -i /usr/local/bin/docker-entrypoint.sh; \
  echo $COMMAND >> /usr/local/bin/tema-entrypoint.sh;

ENTRYPOINT ["tema-entrypoint.sh"]

VOLUME /var/www/html

CMD ["apache2-foreground"]
