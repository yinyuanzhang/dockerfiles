FROM ubuntu:16.04
USER root
RUN apt-get update && \
	apt-get --no-install-recommends -yq -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install apache2 && \
	apt-get --no-install-recommends -yq -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install libmapcache1 && \
	apt-get --no-install-recommends -yq -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install cgi-mapserver && \
	apt-get --no-install-recommends -yq -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install mapserver-bin && \
	apt-get --no-install-recommends -yq -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install mapcache-cgi && \
	apt-get --no-install-recommends -yq -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install mapcache-tools && \
	apt-get --no-install-recommends -yq -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install libapache2-mod-mapcache && \
	apt-get --no-install-recommends -yq -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install build-essential && \
	apt-get --no-install-recommends -yq -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install python-dev && \
	a2enmod cgi && \
	mkdir /tmp/ms_tmp/ && \
	mkdir -p /opt/cache && \
	mkdir -p /opt/mapabase
ADD  ./basemaps /opt/mapabase
COPY ./config/000-default.conf /etc/apache2/sites-available/ 
COPY ./config/ports.conf /etc/apache2/
WORKDIR /opt/mapabase
RUN chmod +x init_osmserver.sh && \
	chgrp -R 0 /opt/mapabase && \
	chmod -R g+rwX /opt/mapabase && \
	chgrp -R 0 /var/log/apache2 && \
	chmod -R g+rwX /var/log/apache2 && \
	chgrp -R 0 /var/run/apache2 && \
	chmod -R g+rwX /var/run/apache2 && \
	chgrp -R 0 /opt/cache && \
	chmod -R g+rwX /opt/cache && \
	chgrp -R 0 /tmp/ms_tmp && \
	chmod -R g+rwX /tmp/ms_tmp && \
	ln -sf /proc/self/fd/1 /var/log/apache2/error.log && \
	ln -sf /proc/self/fd/1 /var/log/apache2/access.log
ENV OSM_HOST=192.168.1.112 \
	OSM_DBNAME=dbspo \
	OSM_USER=postgres \
	OSM_PASSWORD=postgres \
	OSM_PORT=5432 
CMD ["apachectl", "-D", "FOREGROUND"]	
ENTRYPOINT ["/opt/mapabase/init_osmserver.sh"]
USER 1001
EXPOSE 8080
