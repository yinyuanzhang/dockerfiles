FROM nginx:latest

RUN apt update && apt install -y curl

COPY index.html /usr/share/nginx/html/
COPY docker-entrypoint /usr/local/bin/
COPY default.conf /etc/nginx/conf.d/default.conf

ENTRYPOINT ["/usr/local/bin/docker-entrypoint"]
