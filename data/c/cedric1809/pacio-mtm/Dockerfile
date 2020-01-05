FROM centos:8
RUN yum install -y --setopt=tsflags=nodocs httpd composer-cli nodejs php wget git yum-utils php-json php-zip php-pdo php-mbstring php-dom php-gd php-curl php-pgsql
ADD run-httpd.sh /run-httpd.sh
RUN chmod -v +x /run-httpd.sh
CMD ["/run-httpd.sh"]
