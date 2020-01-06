FROM markoshust/magento-nginx:1.13-3

COPY ./certs/ /etc/nginx/ssl/

USER root:root

RUN apt-get update && apt-get -y install \
    iptables \
    sudo

RUN adduser app sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

COPY ./docker-entrypoint.sh /
RUN ["chmod", "+x", "/docker-entrypoint.sh"]
ENTRYPOINT ["/docker-entrypoint.sh"]

USER app:app

EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]