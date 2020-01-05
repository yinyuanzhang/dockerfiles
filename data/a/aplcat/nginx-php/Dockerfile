FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y  
RUN apt-get install -y \  
 software-properties-common \
 supervisor \  
 nginx \  
 php5-fpm \  
 php5-cli \  
 php5-curl \  
 php5-gd \  
 php5-mysql \  
 php5-memcached \  
 php5-mcrypt

# Clean up to reduce container size
RUN apt-get remove --purge -y software-properties-common \  
 && apt-get autoremove -y \  
 && apt-get clean  \
 && apt-get autoclean

RUN echo -n > /var/lib/apt/extended_states  

RUN rm -rf \
 /var/lib/apt/lists/* \  
 /usr/share/man/?? \ 
 /usr/share/man/??_* \
 /etc/nginx/conf.d/* \  
 /etc/nginx/sites-available/default

# Configure php-fpm
RUN sed -e 's/;daemonize = yes/daemonize = no/' -i /etc/php5/fpm/php-fpm.conf  
RUN sed -e 's/;listen\.owner/listen.owner/' -i /etc/php5/fpm/pool.d/www.conf  
RUN sed -e 's/;listen\.group/listen.group/' -i /etc/php5/fpm/pool.d/www.conf

# Configure nginx to not run in daemonized mode
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Fix permissions
RUN usermod -u 1000 www-data \
 && groupmod -g 1000 www-data \
 && chown -Rf www-data:www-data /var/www/

# Configure nginx and Supervisor
ADD ./nginx-vhost.conf /etc/nginx/sites-available/default.conf  
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/default.conf
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisor.conf

VOLUME ["/var/www"]
WORKDIR /var/www

EXPOSE 80 443
CMD ["/usr/bin/supervisord"]  
