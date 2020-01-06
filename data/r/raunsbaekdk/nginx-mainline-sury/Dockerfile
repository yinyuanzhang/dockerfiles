FROM debian:stretch-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && \
	apt-get -y install curl gnupg ca-certificates apt-transport-https

RUN curl -o /etc/apt/trusted.gpg.d/sury_apt.gpg https://packages.sury.org/php/apt.gpg && \
	apt-key add /etc/apt/trusted.gpg.d/sury_apt.gpg

RUN echo "deb https://packages.sury.org/nginx-mainline/ stretch main" > /etc/apt/sources.list.d/nginx-mainline.list

RUN apt-get -y update && \
	apt-get -y install nginx-full libnginx-mod-http-headers-more-filter libnginx-mod-http-geoip2 && \
		rm -rf /var/lib/apt/lists/* && \
		rm -rf /tmp/* && \
		rm -rf /var/tmp/* && \
		rm -rf /var/www/html

RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]