FROM nginx:alpine

# forward request and error logs to docker log collector
#	&& ln -sf /dev/stdout /var/log/nginx/access.log \
#	&& ln -sf /dev/stderr /var/log/nginx/error.log

RUN rm -f /var/log/nginx/access.log \
 && rm -f /var/log/nginx/error.log
