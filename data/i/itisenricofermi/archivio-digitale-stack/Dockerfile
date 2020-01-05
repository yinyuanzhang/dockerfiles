FROM nginx:latest
COPY default.conf.template /etc/nginx/conf.d/default.conf.template

ENV PORT=80 \
  CLIENT=frontend \
  CLIENT_PORT=80 \
  API=backend \
  API_PORT=80

CMD /bin/bash -c "envsubst '\$PORT \$CLIENT \$CLIENT_PORT \$API \$API_PORT' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf" && nginx -g 'daemon off;'
