    
#
FROM ubuntu:bionic
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update && apt-get -y upgrade
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:ondrej/php  
RUN apt-get update
RUN apt-get -y install php7.3
RUN apt-get -y install php-pear php7.3-curl php7.3-dev php7.3-gd php7.3-mbstring php7.3-zip php7.3-mysql php7.3-xml php7.3-soap libapache2-mod-php7.3 php7.3-xml

RUN apt -y install apache2
RUN update-alternatives --set php /usr/bin/php7.3
COPY entrypoint.sh /entrypoint.sh
# Run touch /etc/apache2/conf.d/fqdn
Run apt-get clean
#RUN echo "ServerName localhost" | tee /etc/apache2/conf.d/fqdn
Run echo ServerName localhost >> /etc/apache2/apache2.conf 


# Enable apache mods.
RUN a2enmod php7.3
RUN a2enmod rewrite
RUN a2enmod mpm_prefork php7.3


# Update the PHP.ini file, enable <? ?> tags and quieten logging.
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php/7.3/apache2/php.ini
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING | E_PARSE/" /etc/php/7.3/apache2/php.ini



#ENTRYPOINT [ "/bin/bash", "/vnc/entrypoint.sh" ]
ENTRYPOINT [ "/bin/bash", "/entrypoint.sh" ]
#ENTRYPOINT ["/usr/sbin/apache2", "-k", "start"]


EXPOSE 80
#CMD apachectl -D FOREGROUND
#CMD /usr/sbin/apache2ctl -D FOREGROUND