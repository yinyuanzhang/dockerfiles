FROM aesopagency/nginx:1.0.0

MAINTAINER Aesop Agency <technical@aesopagency.com>

# Apply Nginx configuration
ADD config/phpfpm.conf /opt/etc/phpfpm.conf
ADD config/vhost /etc/nginx/sites-available/vhost

# Nginx startup script
ADD config/nginx-start-phpfpm.sh /opt/bin/nginx-start-phpfpm.sh
RUN chmod u=rwx /opt/bin/nginx-start-phpfpm.sh

ENTRYPOINT ["/opt/bin/nginx-start-phpfpm.sh"]
