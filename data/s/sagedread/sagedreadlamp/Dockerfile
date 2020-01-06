FROM centos:centos7
MAINTAINER Sagecore Technologies “cloud@sagecoretech.com”
 
# Install various utilities
RUN yum -y install curl wget zip unzip \
hostname yum-utils which \
epel-release

# Install Apache
RUN yum -y install httpd

# Reconfigure Apache
RUN sed -i 's/AllowOverride None/AllowOverride All/g' /etc/httpd/conf/httpd.conf \
&& chown root:apache /var/www/html \
&& chmod g+s /var/www/html

# Install Remi Updated PHP 7
RUN wget http://rpms.remirepo.net/enterprise/remi-release-7.rpm \
&& rpm -Uvh remi-release-7.rpm \
&& yum-config-manager --enable remi-php73 \
&& yum -y install php php-gd php-mysqlnd php-pdo php-xml openssl mod_ssl mod_deflate mod_expires php-common php-curl php-mbstring

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer 

#Install WKHTMLTOPDF
RUN wget https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox-0.12.5-1.centos7.x86_64.rpm
RUN yum install -y wkhtmltox-0.12.5-1.centos7.x86_64.rpm

# UTC Timezone & Networking
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime \
	&& echo "NETWORKING=yes" > /etc/sysconfig/network

EXPOSE 80
EXPOSE 3306

ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]