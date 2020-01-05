FROM nginx:1.17.5

COPY default.conf.template /etc/nginx/conf.d/default.conf.template
COPY nginx.conf /etc/nginx/nginx.conf
COPY static-web-app /usr/share/nginx/html

CMD /bin/bash -c "envsubst '\$PORT' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf" && nginx -g 'daemon off;'
