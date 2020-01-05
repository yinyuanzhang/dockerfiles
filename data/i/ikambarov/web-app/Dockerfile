FROM ubuntu
LABEL maintainer="Islam Kambarov (ikambarov@yahoo.com)"
RUN apt-get update && apt-get install -y dnsutils iputils-ping nginx
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log
RUN echo "Web-App Version 2.0.0" > /var/www/html/index.html
EXPOSE 80
ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]

