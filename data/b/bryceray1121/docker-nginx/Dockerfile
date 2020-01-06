FROM ubuntu:trusty

MAINTAINER "Bryce Ray" <bray@rxsavingsllc.com>

#Install Nginx
RUN apt-get update -y && \
    apt-get install -y nginx \
        software-properties-common

RUN adduser --system --no-create-home --disabled-login --disabled-password --group nginx --uid 1000

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx-access.log \
	&& ln -sf /dev/stderr /var/log/nginx-error.log


ADD container-root /
RUN rm /etc/nginx/sites-enabled/default

RUN chmod 755 /config/init/nginx-start.sh

EXPOSE 80 443

CMD ["/config/init/nginx-start.sh"]
