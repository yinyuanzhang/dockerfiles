# Pull base image.
FROM debian:stretch-slim

MAINTAINER Omar Davila <omar@zinobe.com>

ENV PUID=33
ENV PGID=33

ENV WORKDIR=/home/dws

WORKDIR $WORKDIR

VOLUME '/etc/nginx/sites-enabled'
VOLUME '/etc/nginx/ssl'

# Install Nginx
RUN apt-get update; \
    apt-get install -y \
    nginx

ADD ./entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/entrypoint.sh

RUN ln -s /usr/local/bin/entrypoint.sh /entrypoint.sh

EXPOSE 80
EXPOSE 443

# Start nginx
ENTRYPOINT ["/bin/bash", "/usr/local/bin/entrypoint.sh"]