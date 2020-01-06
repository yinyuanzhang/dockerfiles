FROM phusion/baseimage:0.9.18
MAINTAINER Chris Knight <chris@hevnly.com>

# Update the OS
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"

# Surpress Upstart errors/warning
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

# Let the conatiner know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

# Update base image
# Add sources for latest nginx
# Install software requirements
RUN apt-get install -y software-properties-common
RUN nginx=stable && \
add-apt-repository ppa:nginx/$nginx
RUN add-apt-repository ppa:ondrej/php
RUN apt-get update
RUN apt-get upgrade -y --force-yes
RUN BUILD_PACKAGES="unzip nginx php5.6-fpm php5.6-cli php5.6-mysql php5.6-curl php5.6-intl php5.6-xml php5.6-mbstring" && \
apt-get -y --force-yes install $BUILD_PACKAGES
RUN apt-get remove --purge -y software-properties-common
RUN apt-get autoremove -y
RUN apt-get clean
RUN apt-get autoclean
RUN echo -n > /var/lib/apt/extended_states
RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /usr/share/man/??
RUN rm -rf /usr/share/man/??_*

RUN ln -s /usr/bin/python3 /usr/bin/python

# install aws cli
ADD https://s3.amazonaws.com/aws-cli/awscli-bundle.zip /tmp/awscli-bundle.zip
RUN unzip /tmp/awscli-bundle.zip -d /tmp/ && \
/tmp/awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \
rm -rf /tmp/awscli-bundle.zip /tmp/awscli-bundle

# tweak nginx config
RUN sed -i -e"s/worker_processes  1/worker_processes 5/" /etc/nginx/nginx.conf && \
sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf && \
sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf && \
echo "daemon off;" >> /etc/nginx/nginx.conf

# tweak php-fpm config
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php/5.6/fpm/php.ini && \
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g" /etc/php/5.6/fpm/php.ini && \
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" /etc/php/5.6/fpm/php.ini && \
sed -i -e "s/memory_limit\s*=\s*128M/memory_limit = 512M/g" /etc/php/5.6/fpm/php.ini && \
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/5.6/fpm/php-fpm.conf && \
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" /etc/php/5.6/fpm/pool.d/www.conf && \
sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g" /etc/php/5.6/fpm/pool.d/www.conf && \
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g" /etc/php/5.6/fpm/pool.d/www.conf && \
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g" /etc/php/5.6/fpm/pool.d/www.conf && \
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g" /etc/php/5.6/fpm/pool.d/www.conf && \
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g" /etc/php/5.6/fpm/pool.d/www.conf

# fix ownership of sock file for php-fpm
RUN sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g" /etc/php/5.6/fpm/pool.d/www.conf

# nginx site conf
RUN rm -Rf /etc/nginx/conf.d/* && \
rm -Rf /etc/nginx/sites-available/default
ADD conf/nginx-site.conf /etc/nginx/sites-available/default.conf
ADD conf/timed-combined.conf /etc/nginx/conf.d/timed-combined.conf
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/default.conf

RUN mkdir /run/php/

# create startup script
RUN mkdir /etc/service/nginx
ADD scripts/nginx_start.sh /etc/service/nginx/run

RUN mkdir /etc/service/php5-fpm
ADD scripts/php5-fpm_start.sh /etc/service/php5-fpm/run

# Setup Volume
VOLUME ["/var/log/nginx"]

# add test PHP file
ADD src/index.php /var/www/index.php
RUN chown -Rf www-data.www-data /usr/share/nginx/html/

# Expose Ports
EXPOSE 80
