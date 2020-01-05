#Version 0.0.1
FROM alpine:edge

MAINTAINER Alex Vikarchuk <shcoder.alex@gmail.com>

RUN apk add --update unzip nginx bash && \
    rm -rf /var/cache/apk/* && \
    chown -R nginx:www-data /var/lib/nginx

COPY start.sh /bin/start.sh

VOLUME /etc/nginx/conf.d
VOLUME /templates

COPY ./templates/default.ctmpl /templates/default.ctmpl

COPY nginx.conf /etc/nginx/nginx.conf

ADD https://releases.hashicorp.com/consul-template/0.14.0/consul-template_0.14.0_linux_amd64.zip /usr/bin/
RUN unzip -uo /usr/bin/consul-template_0.14.0_linux_amd64.zip -d /usr/local/bin


EXPOSE 80 443
ENTRYPOINT ["/bin/start.sh"]