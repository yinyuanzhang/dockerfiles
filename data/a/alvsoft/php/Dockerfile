FROM appsvctest/php:7.2.1-apache_1801171635
MAINTAINER Azure App Services Container Images <appsvc-images@microsoft.com>

COPY init_container.sh /bin/

RUN yes | pecl install xdebug-beta \
    && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.profiler_output_dir=/home/LogFiles" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && chmod 777 /bin/init_container.sh
    
EXPOSE 9000

# Environment variables
ENV XDEBUG_REMOTE_AUTOSTART=off
ENV XDEBUG_REMOTE_CONNECT_BACK=0
ENV XDEBUG_REMOTE_HOST=localhost

ENTRYPOINT ["/bin/init_container.sh"]