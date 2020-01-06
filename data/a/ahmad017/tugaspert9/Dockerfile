FROM alpine:latest
RUN apk add --update nginx && \
        rm -rf /var/cache/apk/* && \
        mkdir -p /tmp/nginx/

COPY files/nginx.conf /etc/nginx/nginx.conf
COPY files/default.conf /etc/nginx/conf.d/default.conf
ADD files/images/about.jpg /usr/share/nginx/html/images/
ADD files/images/hero.jpg /usr/share/nginx/html/images/
ADD files/index.html /usr/share/nginx/html/
ADD files/style.css /usr/share/nginx/html/

EXPOSE 80/tcp

ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]
