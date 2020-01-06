FROM magento/magento-cloud-docker-nginx:1.9

COPY etc/nginx.conf /etc/nginx/nginx.conf
#COPY etc/vhost.conf /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/conf.d/default.conf

EXPOSE 10080

ENV UPLOAD_MAX_FILESIZE 64M
ENV FPM_HOST fpm
ENV FPM_PORT 9000
ENV MAGENTO_ROOT /var/www/magento
ENV MAGENTO_RUN_MODE production
ENV DEBUG false

RUN touch /var/run/nginx.pid \
 && chown -Rf www-data:www-data \
    /var/run/nginx.pid \
    /var/cache/nginx \
    /var/log/nginx
 
RUN ["chmod", "+x", "/usr/local/bin/docker-environment"]
USER www-data

ENTRYPOINT ["/usr/local/bin/docker-environment"]
CMD ["nginx", "-g", "daemon off;"]
