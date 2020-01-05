FROM nginx:1.10

LABEL maintainer="Rezza Kurniawan <rezza@matamerah.com>"

ARG PHP_UPSTREAM_CONTAINER=app
ARG PHP_UPSTREAM_PORT=9000

COPY nginx.conf /etc/nginx/

RUN echo "upstream php-upstream { server ${PHP_UPSTREAM_CONTAINER}:${PHP_UPSTREAM_PORT}; }" > /etc/nginx/conf.d/upstream.conf \
    && rm /etc/nginx/conf.d/default.conf

ADD ./startup.sh /opt/startup.sh
RUN sed -i 's/\r//g' /opt/startup.sh
CMD ["/bin/bash", "/opt/startup.sh"]

EXPOSE 80 443