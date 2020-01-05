FROM profideo/php-5.6.20-fpm

# Install sass
RUN apt-get install -y rubygems build-essential
RUN gem install sass

# PHP configuration
COPY files/php.ini /usr/local/etc/php/php.ini

# Supervisor
COPY files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]
