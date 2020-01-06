
FROM centos
MAINTAINER CORRA (manish@corra.com)

ENV CERT_FILES_FOLDER ''
ENV NGINX_CONFIG_FILE_PATH ''
ENV CONFIG_D_FILES_FOLDER ''
ENV SKIP_CHOWN true
ENV WEB_ROOT /var/www/html
ENV php_conf /etc/php-fpm.conf
ENV fpm_conf /etc/php-fpm.d/www.conf
ENV fpm_ini /etc/php.ini
ENV GENERATE_CERT 1

RUN yum install -y python-setuptools
RUN easy_install supervisor

#######################################################
###################  INSTALL NGINX  ###################
#######################################################
RUN yum install -y epel-release
RUN yum install -y nginx

#######################################################
###################  INSTALL PHP  ###################
#######################################################
RUN rpm -ivh https://centos7.iuscommunity.org/ius-release.rpm
RUN rpm -Uvh http://yum.newrelic.com/pub/newrelic/el5/x86_64/newrelic-repo-5-3.noarch.rpm

#RUN yum -y install python-pip unzip nano gettext php70u php70u-pdo php70u-mysqlnd php70u-opcache php70u-xml php70u-mcrypt php70u-gd php70u-devel php70u-mysql php70u-intl php70u-mbstring php70u-bcmath php70u-json php70u-iconv php70u-fpm php70u-soap redis
#RUN yum -y install python-pip unzip nano gettext php71u php71u-pdo php71u-mysqlnd php71u-opcache php71u-xml php71u-mcrypt php71u-gd php71u-devel php71u-mysql php71u-intl php71u-mbstring php71u-bcmath php71u-json php71u-iconv php71u-fpm php71u-soap redis
RUN yum -y install python-pip unzip nano gettext php72u php72u-pdo php72u-mysqlnd php72u-opcache php72u-xml php72u-mcrypt php72u-gd php72u-devel php72u-mysql php72u-intl php72u-mbstring php72u-bcmath php72u-json php72u-iconv php72u-fpm php72u-soap php72u-redis redis php72u-devel libmcrypt-devel pecl make gcc git
RUN pecl install mcrypt-1.0.2
#Install AWS CLI
RUN pip install awscli --upgrade --user

# tweak php-fpm config
RUN echo 'extension=mcrypt.so' > /etc/php.d/20-mcrypt.ini
RUN sed -i "s/user = .*/user = nginx/g" ${fpm_conf}
RUN sed -i "s/group = .*/group = nginx/g" ${fpm_conf}
RUN sed -i 's/;catch_workers_output/catch_workers_output/g' ${fpm_conf}
RUN sed -i "s/; error_reporting.*/error_reporting = E_ALL/" ${fpm_ini}
RUN sed -i "s/; display_errors.*/display_errors = On/" ${fpm_ini}
RUN sed -i "s/display_errors = Off/display_errors = On/" ${fpm_ini}
RUN sed -i "s/memory_limit = .*/memory_limit = 768M/" ${fpm_ini}
RUN sed -i "s/;date.timezone =.*/date.timezone = America\/New_York/" ${fpm_ini}
RUN sed -i "s|;session.save_path =.*|session.save_path = $WEB_ROOT/var/session|" ${fpm_ini}

#Copy Default nginx.conf & magento.conf. 
RUN rm -Rf /etc/nginx/nginx.conf
COPY config/nginx.conf /etc/nginx/nginx.conf
RUN rm -rf /etc/nginx/conf.d/default.conf
COPY conf.d/magento.conf.tmpl /etc/nginx/conf.d/magento.conf.tmpl
RUN envsubst '\$WEB_ROOT' < /etc/nginx/conf.d/magento.conf.tmpl > /etc/nginx/conf.d/magento.conf
RUN rm -rf /etc/nginx/conf.d/magento.conf.tmpl


#Install Composer
RUN cd /tmp
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

WORKDIR $WEB_ROOT

#PHPINFO Test file
RUN mkdir -p $WEB_ROOT/pub
RUN mkdir -p $WEB_ROOT/var/log
RUN touch $WEB_ROOT/var/log/system.log
RUN touch $WEB_ROOT/var/log/exception.log

ADD scripts/index.php $WEB_ROOT/pub
RUN chown :nginx $WEB_ROOT/pub/index.php
RUN chmod 775 $WEB_ROOT/pub/index.php



# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log \
	&& ln -sf /dev/stderr /var/log/php-fpm/error.log \
	&& ln -sf /dev/dtderr /var/log/php-fpm/error.log \
	&& ln -sf /dev/dtderr $WEB_ROOT/var/log/system.log \
	&& ln -sf /dev/dtderr $WEB_ROOT/var/log/exception.log 



ADD config/supervisord.conf /etc/supervisord.conf
ADD scripts/start.sh /start.sh
RUN chmod g+x /start.sh


EXPOSE 443 80

CMD ["/start.sh"]
