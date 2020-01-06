FROM mimir02/httpdalpinegitnode
MAINTAINER Jeremy MOREAU

RUN apt-get install -y openrc && apt-get install -y apache2 
RUN rc-update add apache2 default \
&& touch /run/openrc/softlevel

RUN echo '# If you just change the port or add more ports here, you will likely also \n\
# have to change the VirtualHost statement in \n\
# /etc/apache2/sites-enabled/000-default.conf \n\
 \n\
Listen 8080 \n\
 \n\
<IfModule ssl_module> \n\
        Listen 443 \n\
</IfModule> \n\
 \n\
<IfModule mod_gnutls.c> \n\
        Listen 443 \n\
</IfModule> \n\
 \n\
# vim: syntax=apache ts=4 sw=4 sts=4 sr noet \n\
' > /etc/apache2/ports.conf

RUN echo '<VirtualHost *:8080> \n\
        # The ServerName directive sets the request scheme, hostname and port t$ \n\
        # the server uses to identify itself. This is used when creating \n\
        # redirection URLs. In the context of virtual hosts, the ServerName \n\
        # specifies what hostname must appear in the request s Host: header to \n\
        # match this virtual host. For the default virtual host (this file) this \n\
        # value is not decisive as it is used as a last resort host regardless. \n\
        # However, you must set it for any further virtual host explicitly. \n\
        #ServerName www.example.com \n\
 \n\
        ServerAdmin webmaster@localhost \n\
        DocumentRoot /var/www/html \n\
 \n\
        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn, \n\
        # error, crit, alert, emerg. \n\
        # It is also possible to configure the loglevel for particular \n\
        # modules, e.g. \n\
        #LogLevel info ssl:warn \n\
        ErrorLog ${APACHE_LOG_DIR}/error.log \n\
        CustomLog ${APACHE_LOG_DIR}/access.log combined \n\
 \n\
        # For most configuration files from conf-available/, which are \n\
        # enabled or disabled at a global level, it is possible to \n\
        # include a line for only one particular virtual host. For example the \n\
        # following line enables the CGI configuration for this host only \n\
        # after it has been globally disabled with "a2disconf". \n\
        #Include conf-available/serve-cgi-bin.conf \n\
</VirtualHost> \n\
# vim: syntax=apache ts=4 sw=4 sts=4 sr noet \n\
' > /etc/apache2/sites-enabled/000-default.conf

RUN cd /var/www \
&& git clone https://github.com/mimir02/AppliNodeDevOps.git \
&& cd AppliNodeDevOps \
&& git checkout docker-dev

RUN cp -R /var/www/AppliNodeDevOps/* /var/www/html

#CMD kill -USR1 1

#CMD service apache2 restart

WORKDIR /var/www/html