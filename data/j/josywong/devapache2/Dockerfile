FROM phusion/baseimage:0.9.18
MAINTAINER angelics

# Set correct environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV HOME            /root
ENV LC_ALL          C.UTF-8
ENV LANG            en_US.UTF-8
ENV LANGUAGE        en_US.UTF-8
ENV TERM xterm

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Copy files
COPY rootfs/ /tmp/rootfs/

RUN \
	chmod -R +x /tmp/rootfs && \
	cp -R /tmp/rootfs/* / && \
	# Configure user nobody to match unRAID's settings
	usermod -u 99 nobody && \
	usermod -g 100 nobody && \
	usermod -d /home nobody && \
	chown -R nobody:users /home && \
	add-pkg \
		# Install proxy Dependencies
		libapache2-mod-php5 \
		php5-mysqlnd \
		inotify-tools \
		php5-gd \
		php5-imagick \
		curl \
		&& \
	service apache2 restart && \
	rm -R -f /var/www && \
	ln -s /web /var/www && \
	mv /etc/apache2/sites-available/000-default.conf /etc/apache2/000-default.conf && \
	rm /etc/apache2/sites-available/* && \
	rm /etc/apache2/apache2.conf && \
	ln -s /config/proxy-config.conf /etc/apache2/sites-available/000-default.conf && \
	ln -s /var/log/apache2 /logs && \
	# Manually set the apache environment variables in order to get apache to work immediately.
	echo www-data > /etc/container_environment/APACHE_RUN_USER && \
	echo www-data > /etc/container_environment/APACHE_RUN_GROUP && \
	echo /var/log/apache2 > /etc/container_environment/APACHE_LOG_DIR && \
	echo /var/lock/apache2 > /etc/container_environment/APACHE_LOCK_DIR && \
	echo /var/run/apache2.pid > /etc/container_environment/APACHE_PID_FILE && \
	echo /var/run/apache2 > /etc/container_environment/APACHE_RUN_DIR && \
	rm -rf /tmp/* /tmp/.[!.]*
	
# Copy files
COPY conf/ /

# Expose Ports
EXPOSE 80

# The www directory and proxy config location
VOLUME ["/config", "/web", "/logs"]