FROM alpine:latest
LABEL maintainer="Saurabh Sane"
LABEL description="This example DOCKER file installs NGINX"

RUN apk add --update nginx && \
        rm -rf /var/cache/apk/* && \
        mkdir -p /tmp/nginx/

COPY files/nginx.conf /etc/nginx/nginx.conf
COPY files/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80/tcp

ENTRYPOINT ["nginx"]

CMD ["-g", "daemon off;"]
