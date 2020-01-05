FROM centos:6

ENV PROCESSMAKER_VERSION="3.1.3"  PROCESSMAKER_EDITION="-community"

RUN set -x \
    && rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm \
    && rpm -Uvh https://mirror.webtatic.com/yum/el6/latest.rpm \
    && yum -y update \
    && yum -y install httpd php56w mysql55w \
    && yum -y install \
         php56w-mysqlnd \
         php56w-gd \
         php56w-soap \
         php56w-ldap \
         php56w-xml \
         php56w-mbstring \
         php56w-cli \
         php56w-curl \
         php56w-mcrypt \
         php56w-devel \
         php56w-pecl-apcu \
    && yum -y install phpmyadmin wget \
    && yum clean all \
    && true
RUN set -x \
    && wget -O processmaker-${PROCESSMAKER_VERSION}${PROCESSMAKER_EDITION}.tar.gz "https://sourceforge.net/projects/processmaker/files/ProcessMaker/${PROCESSMAKER_VERSION}/processmaker-${PROCESSMAKER_VERSION}${PROCESSMAKER_EDITION}.tar.gz/download" \
    && tar -C /opt -xzf processmaker-3.1.3-community.tar.gz \
    && cd /opt/processmaker \
    && chmod -R 770 shared workflow/public_html gulliver/js gulliver/thirdparty/html2ps_pdf/cache \
    && cd workflow/engine/ \
    && chmod -R 770 config content/languages plugins xmlform js/labels \
    && chown -R apache:apache /opt/processmaker \
    && true
RUN set -x \
    && ln -sf /dev/stdout /var/log/httpd/access_log \
    && ln -sf /dev/stdout /var/log/httpd/error_log \
    && ( \ \
       echo 'file_uploads = On'; \
       echo 'short_open_tag = On'; \
       echo 'memory_limit = 512M'; \
       echo 'error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT'; \
       echo 'display_errors = Off'; \
       echo 'post_max_size = 24M'; \
       echo 'upload_max_filesize = 24M'; \
    ) >> /etc/php.ini \
    && rm -f /etc/httpd/conf.d/welcome.conf \
    && echo 'ServerName 127.0.0.1' >> /etc/httpd/conf/httpd.conf \
    && sed -e 's@/example/path/to/@/opt/@g' -e 's/\(Require all granted\)/# \1/' /opt/processmaker/pmos.conf.example > /etc/httpd/conf.d/pmos.conf \
    && echo "SELINUX=disabled" > /etc/selinux/config  \
    && echo "SELINUXTYPE=targeted" >> /etc/selinux/config \
    && true

EXPOSE 80
VOLUME "/opt/processmaker/shared"
WORKDIR "/opt/processmaker"

CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
