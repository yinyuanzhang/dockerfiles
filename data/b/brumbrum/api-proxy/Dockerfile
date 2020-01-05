FROM brumbrum/base
LABEL maintainer="alessandro.lattao@brumbrum.it"

# Let the conatiner know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

RUN \
  apt-get -y --no-install-recommends install nginx iputils-ping libnginx-mod-http-headers-more-filter gettext-base bind9 dnsutils vim && \
  apt-get -y autoclean && \
  apt-get -y clean && \
  apt-get -y autoremove

# Expose Ports
EXPOSE 80
EXPOSE 53/tcp
EXPOSE 53/udp

# Configuro i framework
ADD /etc/nginx/sites-available /etc/nginx/sites-available

# Configuro bind9 e imposto l'output su stdout
ADD /etc/bind/named.conf.options /etc/bind/named.conf.options
ADD /etc/bind/named.conf.local /etc/bind/named.conf.local
ADD /etc/bind/db.brumbrum.network.orig /etc/bind/db.brumbrum.network.orig
RUN sed -i -e 's/-u bind/-u bind -g/g' /etc/default/bind9

# Aggiungo gli script pre e post entrypoint
COPY entrypoint.pre-run.d/* /entrypoint.pre-run.d/

# Do il permesso di esecuzione sui file altrimenti run-parts non li avvia
RUN chmod +x /entrypoint.pre-run.d/*

# Aggiungo l'entrypoint
ADD entrypoint.sh /entrypoint.sh
RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT ["/entrypoint.sh"]
