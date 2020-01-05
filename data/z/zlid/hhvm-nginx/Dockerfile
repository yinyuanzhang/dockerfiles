FROM dcoxall/debian
MAINTAINER Yuriy Safargaliev nekto.ryadom@gmail.com
RUN echo deb http://dl.hhvm.com/debian wheezy main | tee /etc/apt/sources.list.d/hhvm.list
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y --force-yes install  hhvm-fastcgi nginx php5 php5-common
ADD default /etc/nginx/sites-enabled/default
ADD index.php /var/www/index.php
RUN chown www-data:www-data /var/www/index.php
ADD run.sh /run.sh
EXPOSE 80:80
CMD ["/run.sh", "-D"