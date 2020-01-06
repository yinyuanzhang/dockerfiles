FROM krosh961/alpine3.7-docker

MAINTAINER Sergey Kardashov <krosh961@yandex.ru>


LABEL org.label-schema.name="apache-alpine3.7" \
      org.label-schema.description="This is a micro docker container based on Alpine 3.7, Apache 2.4" \
      org.label-schema.url="https://hub.docker.com/r/krosh961/apache-alpine3.7/" \
      org.label-schema.vcs-url="https://github.com/krosh961/apache-alpine3.7" 


COPY root/. /

RUN apk update && apk upgrade && \
    # Make info file about this build
    printf "Build of krosh961/apache-alpine3.7, date: %s\n"  `date -u +"%Y-%m-%dT%H:%M:%SZ"` >> /etc/BUILD && \
    apk add apache2 libxml2-dev apache2-utils && \
    mkdir /web/ && chown -R apache.www-data /web && \
    sed -i 's#^DocumentRoot ".*#DocumentRoot "/web/html"#g' /etc/apache2/httpd.conf && \
    sed -i 's#AllowOverride [Nn]one#AllowOverride All#' /etc/apache2/httpd.conf && \
    sed -i 's#^ServerRoot .*#ServerRoot /web#g'  /etc/apache2/httpd.conf && \
    sed -i 's/^#ServerName.*/ServerName webproxy/' /etc/apache2/httpd.conf && \
    sed -i 's#^IncludeOptional /etc/apache2/conf#IncludeOptional /web/config/conf#g' /etc/apache2/httpd.conf && \
    sed -i 's#PidFile "/run/.*#Pidfile "/web/run/httpd.pid"#g'  /etc/apache2/conf.d/mpm.conf && \
    sed -i 's#Directory "/var/www/localhost/htdocs.*#Directory "/web/html" >#g' /etc/apache2/httpd.conf && \
    sed -i 's#Directory "/var/www/localhost/cgi-bin.*#Directory "/web/cgi-bin" >#g' /etc/apache2/httpd.conf && \
    sed -i 's#/var/log/apache2/#/web/logs/#g' /etc/logrotate.d/apache2 && \
    sed -i 's/Options Indexes/Options /g' /etc/apache2/httpd.conf && \
    sed -i '/LoadModule rewrite_module/s/^#//g' /etc/apache2/httpd.conf && \
    rm -rf /var/cache/apk/*

EXPOSE 80 443

