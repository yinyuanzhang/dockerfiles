FROM ampache/ampache
LABEL Maintainer Mue


# Danke :) Sehr coole Idee! 
# https://github.com/hyperactivated/ampache-sonos

WORKDIR /var/www

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install git && \
#   Sonos Zusatz von GitHub laden -> jetzt eigene Version!
    git clone https://github.com/mueee/ampache-sonos.git && \
#   git clone https://github.com/hyperactivated/ampache-sonos.git && \
    echo ServerName localhost >> /etc/apache2/apache2.conf
    
    
