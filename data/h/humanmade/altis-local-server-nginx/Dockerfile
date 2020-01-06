ARG FROM_NGINX=1.17
FROM nginx:${FROM_NGINX}-alpine
LABEL Maintainer="Nathaniel Schweinberg <nathaniel@humanmade.com>"

RUN mkdir -p /etc/nginx/ssl
COPY tls.key /etc/nginx/ssl/tls.key
COPY tls.crt /etc/nginx/ssl/tls.crt
COPY dhparam.pem /etc/nginx/ssl/dhparam.pem
RUN chmod +r /etc/nginx/ssl/tls.key

# Configure nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY nginx-fastcgi_params.conf /etc/nginx/fastcgi_params
COPY nginx-fastcgi_settings.conf /etc/nginx/fastcgi_settings

RUN mkdir -p /usr/src/app \
	&& mkdir -p /var/cache/nginx/client_temp /var/cache/nginx/proxy_temp \
	&& chown -R nginx:nginx /var/cache/nginx \
	&& touch /var/run/nginx.pid /var/run/nginx.lock \
	&& chown -R nginx:nginx /var/log/nginx /var/run/nginx.pid /var/run/nginx.lock \
	&& chmod -R +rwx /var/run/nginx.pid /var/run/nginx.lock \
	&& rm -rf /etc/nginx/conf.d/default.conf

RUN addgroup nginx www-data

USER nginx
EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
