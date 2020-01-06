FROM mendersoftware/api-gateway:2.0.0

COPY entrypoint.sh /entrypoint.sh
COPY nginx.conf /usr/local/openresty/nginx/conf/nginx.conf

RUN chmod +x /entrypoint.sh
