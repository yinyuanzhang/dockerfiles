FROM quay.io/alexcheng1982/apache2-php7:7.0.32

LABEL based_on="alexcheng/magento2"
LABEL maintainer="alberto.v.f.n@gmail.com"
LABEL php_version="7.0.32"
LABEL description="Apache with PHP 7.0.32 and SSH"

ENV INSTALL_DIR /var/www/html
ENV PORT 80
ENV SSH_PORT 2222
EXPOSE 2222 80

#nano adicionado para faciliar qualquer teste
RUN requirements="libpng12-dev libmcrypt-dev libmcrypt4 libcurl3-dev libfreetype6 libjpeg-turbo8 libjpeg-turbo8-dev libpng12-dev libfreetype6-dev libicu-dev libxslt1-dev unzip openssh-server nano" \
    && apt-get update \
    && apt-get install -y $requirements \
    && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && docker-php-ext-install mcrypt \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install zip \
    && docker-php-ext-install intl \
    && docker-php-ext-install xsl \
    && docker-php-ext-install soap \
    && requirementsToRemove="libpng12-dev libmcrypt-dev libcurl3-dev libpng12-dev libfreetype6-dev libjpeg-turbo8-dev" \
    && apt-get purge --auto-remove -y $requirementsToRemove
	
	
#copiando arquivo de inicializacao
COPY init_container.sh /bin/	
#limpando clrf do windows
RUN sed -i -e 's/\r$//' /bin/init_container.sh
#corrigindo permissoes e configurando usuario ssh
RUN chmod 755 /bin/init_container.sh \    
    && echo "root:Docker!" | chpasswd 
	
# configuracao sshd
RUN rm -f /etc/ssh/sshd_config	 
COPY sshd_config /etc/ssh/
COPY ssh_setup.sh /tmp
	
RUN chsh -s /bin/bash www-data

RUN a2enmod rewrite
RUN echo "memory_limit=2048M" > /usr/local/etc/php/conf.d/memory-limit.ini

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY sshd_config /etc/ssh/

WORKDIR $INSTALL_DIR

# Add cron job
# ADD crontab /etc/cron.d/magento2-cron
# RUN chmod 0644 /etc/cron.d/magento2-cron \
#    && crontab -u www-data /etc/cron.d/magento2-cron
	
ENTRYPOINT ["/bin/init_container.sh"]	