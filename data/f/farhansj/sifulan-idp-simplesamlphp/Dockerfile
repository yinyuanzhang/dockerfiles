FROM centos:7
MAINTAINER Muhammad Farhan Sjaugi <farhan@sifulan.my>
LABEL Vendor="SIFULAN Malaysian Access Federation"\
	License=GPLv2 \
	Version=0.1

ENTRYPOINT [ "/init" ]

# Install HTTPD with PHP Support
RUN yum install -y epel-release \
	&& yum -y update \
	&& yum install -y curl crontabs initscripts ntp bc wget certbot httpd mod_ssl php php-mcrypt php-xml php-pdo php-mbstring php-ldap \
	&& yum -y clean all

RUN ntpdate ntpdate asia.pool.ntp.org
RUN cd /var/www/ \
	&& wget "https://github.com/simplesamlphp/simplesamlphp/releases/download/v1.16.2/simplesamlphp-1.16.2.tar.gz" -O simplesamlphp-1.16.2.tar.gz \
	&& tar -zxf simplesamlphp-1.16.2.tar.gz \
	&& mv simplesamlphp-1.16.2 simplesamlphp

# Install tini init
ENV TINI_VERSION v0.10.0
RUN curl -L https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini > /usr/bin/tini \
        && chmod +x /usr/bin/tini


COPY ssp-theme-generator.sh /var/www/simplesamlphp/ssp-theme-generator.sh
COPY simplesamlphp.conf /etc/httpd/conf.d/simplesamlphp.conf
COPY authsources.php /var/www/simplesamlphp/config/authsources.php
COPY init /
COPY config-metarefresh.php /var/www/simplesamlphp/config/config-metarefresh.php
COPY config.php /var/www/simplesamlphp/config/config.php
COPY module_cron.php /var/www/simplesamlphp/config/module_cron.php
