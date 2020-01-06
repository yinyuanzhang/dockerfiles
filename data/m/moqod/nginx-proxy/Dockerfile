FROM jwilder/nginx-proxy
MAINTAINER Artyom Nosov <chip@unixstyle.ru>
RUN echo "client_max_body_size 512M;" >> /etc/nginx/conf.d/moqod-local.conf
RUN echo "proxy_read_timeout 600s;" >> /etc/nginx/conf.d/moqod-local.conf
RUN echo "proxy_send_timeout 600s;" >> /etc/nginx/conf.d/moqod-local.conf
RUN echo "uwsgi_read_timeout 600s;" >> /etc/nginx/conf.d/moqod-local.conf
RUN echo "uwsgi_send_timeout 600s;" >> /etc/nginx/conf.d/moqod-local.conf
