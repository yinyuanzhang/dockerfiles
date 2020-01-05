FROM debian:stretch

RUN apt-get update && apt-get --yes install git
RUN git clone https://penniman26@bitbucket.org/penniman26/mod_auth_openidc_lwa_fork.git /source

RUN cd /source && apt-get --yes install autoconf curl pkg-config libcurl4-openssl-dev libssl-ocaml-dev libjansson-dev libcjose-dev libpcre3-dev make apache2-dev apache2 ruby ruby-dev
RUN gem install sys-filesystem

RUN cd /source && autoconf
RUN cd /source && autoreconf
RUN cd /source && ./configure --with-apxs2=/usr/bin/apxs2
RUN cd /source && make
RUN cd /source && make install

RUN rm -rf /etc/apache2/
RUN git clone https://penniman26@bitbucket.org/penniman26/centralraspberrypiconnectedhomeapacheserverconfig.git /etc/apache2

RUN apt-get install --yes php

RUN rm -rf /var/www/html/
RUN git clone https://penniman26@bitbucket.org/penniman26/centralraspberrypiconnectedhomeapacheserverfiles.git /var/www/html

ENV NODE_SERVER_ADDRESS http://nodejsserver:9999/

CMD /usr/sbin/apachectl start && tail -f /dev/null
