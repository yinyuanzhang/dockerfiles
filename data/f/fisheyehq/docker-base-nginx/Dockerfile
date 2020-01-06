FROM nginx:1.13

RUN groupadd -g 1000 app \
 && useradd -g 1000 -u 1000 -d /var/www -s /bin/bash app
RUN touch /var/run/nginx.pid
RUN mkdir /sock

RUN apt-get update && apt-get install -y \
    openssl \
    iptables \
    sudo

RUN adduser app sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

RUN mkdir /etc/nginx/certs

RUN mkdir /etc/nginx/errors

RUN chown -R app:app /etc/nginx/certs /etc/nginx/errors /sock /var/cache/nginx/ /var/run/nginx.pid /sock

COPY ./conf/ /etc/nginx/

COPY ./docker-entrypoint.sh /
RUN ["chmod", "+x", "/docker-entrypoint.sh"]
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 443

USER app:app

VOLUME /var/www

WORKDIR /var/www/html

CMD ["nginx", "-g", "daemon off;"]
