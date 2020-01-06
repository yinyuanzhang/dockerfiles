FROM centos:6.8

MAINTAINER NgIT "docker@ngit.solutions"

#
# Install SCL repo
#
RUN yum install -y centos-release-SCL

#	
# UPDATE PACKAGES
#
RUN yum update -y

#
# Add Epel Mirror
#
RUN yum install -y epel-release wget

#
# Add Remi Mirro
#
RUN wget http://rpms.famillecollet.com/enterprise/remi-release-6.rpm
RUN rpm -Uvh remi-release-6*.rpm

#
# TOOLS
#
RUN yum install -y curl unzip yum-utils python-setuptools git nmap vim ImageMagick ImageMagick-devel

#
# APACHE
#
RUN yum install -y httpd

#
# PHP
#
RUN yum install -y php54 php54-php php54-php-gd php54-php-mbstring php54-php-mysql php54-php-cli php54-mysql php54-pear

# Enable PHP command line
RUN source /opt/remi/php54/enable

RUN ln -s /opt/remi/php54/enable /etc/profile.d/rh-php54.sh

# Install composer
WORKDIR /tmp
RUN curl -sS https://getcomposer.org/installer | php54
RUN mv /tmp/composer.phar /usr/local/bin/composer
RUN chmod +x /usr/local/bin/composer

#rever o phpmyadmin !!

#RUN php54-pear install pecl/imagick

# Create phpinfo file
RUN echo '<?php phpinfo(); ?>' >> /var/www/html/phpinfo.php

# Allow Access to phpMyAdmin from everyone
#RUN sed -i -e "s/Allow from 127.0.0.1/Allow from ALL/" /etc/httpd/conf.d/phpMyAdmin.conf

# Move old PHP
#RUN mv /etc/httpd/conf.d/php.conf /etc/httpd/conf.d/php53.off

# Copy php.ini to etc
RUN cp /opt/remi/php54/root/etc/php.ini /etc/.

# Configure php.ini
RUN sed -i -e "s/short_open_tag = Off/short_open_tag = On/" /etc/php.ini
RUN sed -i -e "s/short_open_tag = Off/short_open_tag = On/" /opt/remi/php54/root/etc/php.ini

# Return WORKDIR
WORKDIR /

#
# MYSQL
#
RUN yum install -y mysql-server 

## CLEAN UP
RUN package-cleanup --dupes
RUN package-cleanup --cleandupes
RUN yum clean all

#
# Start services for the first time
#
RUN service mysqld start
RUN service httpd start

#
# Tesseract
#
RUN yum install -y gcc gcc-c++ make autoconf automake libtool libjpeg-devel libpng-devel libtiff-devel zlib-devel
RUN mkdir -p /usr/src/tesseract
COPY leptonica-1.71.tar.gz /usr/src/tesseract/
COPY tesseract-3.04.01.tar.gz /usr/src/tesseract/
RUN tar zxf /usr/src/tesseract/leptonica-1.71.tar.gz -C /usr/src/tesseract/
RUN tar zxf /usr/src/tesseract/tesseract-3.04.01.tar.gz -C /usr/src/tesseract/

WORKDIR usr/src/tesseract/leptonica-1.71
RUN pwd
RUN ./configure
RUN make
RUN make install

WORKDIR /usr/src/tesseract/tesseract-3.04.01
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install
RUN ldconfig

WORKDIR /usr/src/tesseract
RUN pwd
RUN git clone https://github.com/tesseract-ocr/tessdata.git
WORKDIR /usr/src/tesseract/tessdata
RUN pwd
RUN mv *.traineddata /usr/local/share/tessdata/

#
# SUPERVISOR
#
RUN easy_install supervisor
RUN mkdir -p /etc/supervisor/conf.d
RUN /usr/bin/echo_supervisord_conf > /etc/supervisor/supervisord.conf
RUN sed -i -e "s/^nodaemon=false/nodaemon=true/" /etc/supervisor/supervisord.conf
ADD supervisor/ /etc/supervisor/conf.d/
RUN echo "[include]" >> /etc/supervisor/supervisord.conf
RUN echo "files=/etc/supervisor/conf.d/*.conf" >> /etc/supervisor/supervisord.conf

EXPOSE 80 3306

#
# Start Supervisor in foreground
#
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]