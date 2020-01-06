FROM debian:stretch-slim
LABEL maintainer=it-devops@pixartprinting.com

RUN ln -snf /usr/share/zoneinfo/Europe/Rome /etc/localtime && \
    echo Europe/Rome > /etc/timezone && \
    apt-get update && \
    apt-get install -y \
        ca-certificates \
        nginx && \
    apt-get clean && \
    rm -fr /usr/local/etc/php-fpm.d && \
    rm -rf /var/lib/apt/lists/*

COPY cert.crt /tmp/cert.crt
RUN cp /tmp/cert.crt /usr/local/share/ca-certificates/ && \
    update-ca-certificates

COPY conf/nginx.conf /etc/nginx/
COPY conf/proxyfcgi.conf /etc/nginx/conf.d/

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

COPY entrypoint.sh /bin/
RUN chmod 755 /bin/entrypoint.sh
ENTRYPOINT ["/bin/entrypoint.sh"]
WORKDIR /var/www
EXPOSE 9001
CMD ["nginx", "-g", "daemon off;"]
