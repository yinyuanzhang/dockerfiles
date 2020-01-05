ARG DOCKER_TAG
FROM brumbrum/base:$DOCKER_TAG
MAINTAINER Alessandro Lattao <alessandro.lattao@brumbrum.it>

RUN \
  apt-get update && \
  apt-get -y --no-install-recommends install nginx libnginx-mod-http-headers-more-filter rsyslog libnginx-mod-http-lua && \
  apt-get -y autoclean && \
  apt-get -y clean && \
  apt-get -y autoremove

# Expose Ports
EXPOSE 80

# Configuro i framework
ADD /etc/nginx/sites-available /etc/nginx/sites-available

# Aggiungo i certificati
COPY etc/ssl/certs/www.brumbrum.it.crt /etc/ssl/certs/www.brumbrum.it.crt
COPY etc/ssl/certs/www.brumbrum.it.key /etc/ssl/certs/www.brumbrum.it.key

# Configurazione di nginx
ADD etc/nginx/nginx.conf /etc/nginx/nginx.conf

# Configurazione di uwsgi
ADD etc/nginx/uwsgi_params /etc/nginx/uwsgi_params

# Configuro rsyslog
ADD etc/rsyslog.conf /etc/rsyslog.conf
ADD etc/rsyslog.d/50-default.conf /etc/rsyslog.d/50-default.conf

# Avvio l'entrypoint
ADD bin/entrypoint.sh /entrypoint.sh
RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT ["/entrypoint.sh"]
