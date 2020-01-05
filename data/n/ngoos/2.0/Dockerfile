FROM centos:7
LABEL Name=Ngoos Version=2.0
MAINTAINER zjhong < zjhong@ngoos.org>

RUN yum install -y --setopt=tsflags=nodocs https://centos7.iuscommunity.org/ius-release.rpm && \
    yum install -y --setopt=tsflags=nodocs \
      wget \
      apache \
      php71u \
      php71u-cli \
      php71u-mysqlnd \
      php71u-gd \
      php71u-soap \
      php71u-apcu \
      php71u-opcache \
      php71u-xml \
      php71u-json \
      php71u-mbstring \
      GraphicsMagick && \
    echo -e "always_populate_raw_post_data = -1;\nmax_execution_time = 240;\nmax_input_vars = 1500;\nupload_max_filesize = 10M;\npost_max_size = 10M;" > /etc/php.d/99-typo3.ini && \
    echo -e "DocumentRoot \"/var/www/site/web\"\n<Directory \"/var/www/site/web\">\nSetEnv TYPO3_CONTEXT ${TYPO3_CONTEXT}\nEnableSendfile off\nEnableMMAP off\nOptions Indexes FollowSymLinks\nAllowOverride All\nOrder allow,deny\nAllow from all\n</Directory>" > /etc/httpd/conf.d/typo3.conf && \
    mkdir -p /var/www/site/web && chown -R apache:apache /var/www/site/ && \
    yum clean all && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer && \
    curl -sSL https://deployer.org/deployer.phar -o /usr/bin/deployer && chmod +x /usr/bin/deployer

RUN cd /var/www/site/web && \
    wget -O - http://121.40.26.71/ngoos-2.0.20170805.tar.gz | tar -xzf - && \
    mv _.htaccess .htaccess && \
    touch FIRST_INSTALL && \
    chown -R apache:apache /var/www/site/
	
RUN rm -rf /etc/localtime && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime 
RUN yum -y install kde-l10n-Chinese && yum -y reinstall glibc-common  
RUN localedef -c -f UTF-8 -i zh_CN zh_CN.utf8
ENV LC_ALL zh_CN.utf8 
ENV TYPO3_CONTEXT Production
EXPOSE 80
WORKDIR /var/www/site
VOLUME /var/www/site/web
CMD httpd -DFOREGROUND
