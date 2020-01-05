# Shinken Docker installation using pip (latest)
FROM        debian:stretch
MAINTAINER  DindonSama

# Install Shinken, Nagios plugins, apache2 and supervisord
RUN         apt-get update && apt-get install -y python-pip \
                python-pycurl \
                python-cherrypy3 \
                nagios-plugins \
                libsys-statistics-linux-perl \
                apache2 \
		ssh \
                supervisor \
                libssl-dev \
                python-crypto \
                inotify-tools \
                ntp \
		curl \
		wget \
		influxdb-client \
		tar

RUN 		pip install influxdb

RUN		cp /usr/share/zoneinfo/Europe/Paris /etc/localtime

RUN         useradd --create-home shinken && \
                wget https://github.com/naparuba/shinken/archive/2.4.3.tar.gz && \
		tar -xvzf 2.4.3.tar.gz && \
		cd shinken-2.4.3 && \
		python setup.py install && \
		ln -s /usr/lib/nagios/plugins/utils.pm /usr/share/perl5

# Install shinken modules from shinken.io
RUN         chown -R shinken:shinken /etc/shinken/ && \
                su - shinken -c 'shinken --init' && \
                su - shinken -c 'shinken install webui' && \
                su - shinken -c 'shinken install auth-htpasswd' && \
                su - shinken -c 'shinken install sqlitedb' && \
                su - shinken -c 'shinken install pickle-retention-file-scheduler' && \
                su - shinken -c 'shinken install booster-nrpe' && \
                su - shinken -c 'shinken install logstore-sqlite' && \
                su - shinken -c 'shinken install livestatus'

# Install and configure thruk
RUN         curl -s "https://labs.consol.de/repo/stable/RPM-GPG-KEY" | apt-key add - && \
		echo "deb http://labs.consol.de/repo/stable/debian stretch main" > /etc/apt/sources.list.d/labs-consol-stable.list && \
                apt-get update && \
                apt-get install -y thruk && \
                apt-get clean
ADD         thruk/thruk_local.conf /etc/thruk/thruk_local.conf

# Install check_nrpe plugin
ADD         nrpe-3.2.1.tar.gz /usr/src/
RUN         cd /usr/src/nrpe-3.2.1/ && \
                ./configure --with-nagios-user=shinken --with-nagios-group=shinken --with-nrpe-user=shinken --with-nrpe-group=shinken --with-ssl=/usr/bin/openssl --with-ssl-lib=/usr/lib/x86_64-linux-gnu && \
                make all && \
                make install-plugin && \
                mv /usr/local/nagios/libexec/check_nrpe /usr/lib/nagios/plugins/check_nrpe && \
                cd / && \
                rm -rf /usr/src/nrpe-2.15

# Configure apache
ADD         shinken/shinken_apache.conf /etc/apache2/conf.d/shinken_apache.conf
RUN	    /usr/sbin/a2enmod proxy proxy_balancer proxy_ftp proxy_html xml2enc
RUN 	    echo 'RedirectMatch ^/$ /thruk/' >> /etc/apache2/conf-available/thruk.conf
RUN 	    a2enmod ldap auth_basic authnz_ldap authz_user

# Configure Shinken modules
ADD         shinken/shinken.cfg /etc/shinken/shinken.cfg
ADD         shinken/broker-master.cfg /etc/shinken/brokers/broker-master.cfg
ADD         shinken/poller-master.cfg /etc/shinken/pollers/poller-master.cfg
ADD         shinken/scheduler-master.cfg /etc/shinken/schedulers/scheduler-master.cfg
ADD         shinken/webui2.cfg /etc/shinken/modules/webui2.cfg
ADD         shinken/livestatus.cfg /etc/shinken/modules/livestatus.cfg
RUN         mkdir -p /etc/shinken/custom_configs /usr/local/custom_plugins && \
                ln -sf /etc/shinken/custom_configs/htpasswd.users /etc/shinken/htpasswd.users && \
                rm -f /etc/thruk/htpasswd && \
                ln -sf /etc/shinken/htpasswd.users /etc/thruk/htpasswd && \
                chown -R shinken:shinken /etc/shinken/
ADD	    custom_configs/htpasswd.users /etc/shinken/custom_configs/htpasswd.users

# Add shinken config watcher to restart arbiter, when changes happen
ADD         shinken/watch_shinken_config.sh /usr/bin/watch_shinken_config.sh
RUN         chmod 755 /usr/bin/watch_shinken_config.sh

# Copy extra NRPE plugins and fix permissions
ADD         extra_plugins/* /usr/lib/nagios/plugins/
RUN         cd /usr/lib/nagios/plugins/ && \
                chmod a+x * && \
                chmod u+s check_apt restart_service check_ping check_icmp check_fping apt_update

# Define mountable directories
VOLUME      ["/etc/thruk", "/var/lib/thruk", "/etc/shinken", "/var/lib/shinken", "/usr/local/custom_plugins"]

# configure supervisor
ADD         supervisor/conf.d/* /etc/supervisor/conf.d/

# Expost port 80 (apache2)
EXPOSE  80

# Default docker process
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]
