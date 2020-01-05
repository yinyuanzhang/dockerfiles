FROM netroby/docker-hhvm
RUN apt-get update ; \
        apt-get install -y wget ;\
        apt-get clean all ;\
        rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate -c https://github.com/phpmyadmin/phpmyadmin/archive/RELEASE_4_6_1.tar.gz; \
        tar zxvf RELEASE_4_6_1.tar.gz;\
        mv phpmyadmin-RELEASE_4_6_1 /www/public; \
        unlink *.tar.gz

COPY config.inc.php /www/public/config.inc.php
