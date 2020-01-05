FROM redis:3
MAINTAINER Elliot Morales <elliot@brutalsys.com >

# Enviroment Variable
ENV NEWRELIC_LICENSE    false
ENV NEWRELIC_APP        false
ENV PHP_CHILDREN        false
ENV TERM				xterm

# Surpress Upstart errors/warning
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

# Let the conatiner know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

# Update base image
# Add sources for latest nginx
# Install software requirements
RUN cd /tmp/ && wget -O - http://nginx.org/keys/nginx_signing.key | apt-key add - && \
codename=$(dpkg --status tzdata|grep Provides|cut -f2 -d'-') && \
echo "deb http://nginx.org/packages/debian/ $codename nginx">/etc/apt/sources.list.d/nginx.list && \
echo "deb-src http://nginx.org/packages/debian/ $codename nginx">>/etc/apt/sources.list.d/nginx.list
RUN apt-get update && \
apt-get update && \
apt-get upgrade -y && \
BUILD_PACKAGES="supervisor nginx php5-fpm git php5-mysql php-apc php5-curl php5-gd php5-intl php5-mcrypt php5-memcache php5-sqlite php5-tidy php5-xmlrpc php5-xsl php5-pgsql php5-mongo php5-redis pwgen wget" && \
apt-get -y install $BUILD_PACKAGES && \
apt-get autoremove -y && \
apt-get clean && \
apt-get autoclean && \
echo -n > /var/lib/apt/extended_states && \
rm -rf /var/lib/apt/lists/* && \
rm -rf /usr/share/man/?? && \
rm -rf /usr/share/man/??_*

# tweak nginx config
RUN sed -i -e"s/worker_processes  1/worker_processes 5/" /etc/nginx/nginx.conf && \
sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf && \
sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf && \
echo "daemon off;" >> /etc/nginx/nginx.conf

# tweak php-fpm config
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php5/fpm/php.ini && \
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g" /etc/php5/fpm/php.ini && \
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" /etc/php5/fpm/php.ini && \
sed -i -e "s/disable_functions/;disable_functions/g" /etc/php5/fpm/php.ini && \
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" /etc/php5/fpm/php.ini && \
sed -i -e "s/short_open_tag = Off/short_open_tag = On/g" /etc/php5/fpm/php.ini && \
sed -i -e "s/short_open_tag = Off/short_open_tag = On/g" /etc/php5/cli/php.ini && \
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf && \
sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g" /etc/php5/fpm/pool.d/www.conf && \
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g" /etc/php5/fpm/pool.d/www.conf && \
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g" /etc/php5/fpm/pool.d/www.conf && \
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g" /etc/php5/fpm/pool.d/www.conf && \
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g" /etc/php5/fpm/pool.d/www.conf && \
sed -i -e "s/log_errors = On/log_errors = Off/g" /etc/php5/fpm/php.ini

# fix ownership of sock file for php-fpm
RUN sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g" /etc/php5/fpm/pool.d/www.conf && \
find /etc/php5/cli/conf.d/ -name "*.ini" -exec sed -i -re 's/^(\s*)#(.*)/\1;\2/g' {} \;

# nginx site conf
RUN rm -Rf /etc/nginx/conf.d/* && \
mkdir -p /etc/nginx/ssl/
ADD ./nginx-site.conf /etc/nginx/conf.d/default.conf

# Install and Configure Newrelic
RUN sed -i 's/^# \(.*-backports\s\)/\1/g' /etc/apt/sources.list && \
    wget -O - https://download.newrelic.com/548C16BF.gpg | apt-key add - && \
    echo "deb http://apt.newrelic.com/debian/ newrelic non-free" > /etc/apt/sources.list.d/newrelic.list && \
    apt-get update -qqy
RUN apt-get install newrelic-php5 -y

# Add static PHP-FPM Config
ADD ./www.conf /etc/php5/fpm/pool.d/www.conf

# Supervisor Config
ADD ./supervisord.conf /etc/supervisord.conf

# Start Supervisord
ADD ./start.sh /start.sh
RUN chmod 755 /start.sh

# ADD PCNTL SUPPORT
RUN codename=$(dpkg --status tzdata|grep Provides|cut -f2 -d'-') && \
echo "deb-src http://httpredir.debian.org/debian $codename main"> /etc/apt/sources.list.d/sources.list && \
apt-get update && \
apt-get -qy install php5-dev && \
mkdir -p /tmp/php && cd /tmp/php && \
apt-get -qy source php5 &&\
cd php*/ext/pcntl && \
phpize && ./configure && make && make install && \
echo "extension=pcntl.so">/etc/php5/fpm/conf.d/20-pcntl.ini && \
cd / && rm -rvf /tmp/php && apt-get -qy purge dpkg-dev php5-dev && \
rm -f /etc/apt/sources.list.d/sources.list && \
apt-get -qy clean

# add test PHP file
# ADD ./index.php /usr/share/nginx/html/index.php
RUN chown -Rf nginx.nginx /usr/share/nginx/html/
COPY redis.conf /usr/local/etc/redis/redis.conf

# Expose Ports
EXPOSE 443
EXPOSE 80
EXPOSE 6379

CMD ["/bin/bash", "/start.sh"]
