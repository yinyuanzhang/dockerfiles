FROM ubuntu:xenial

USER root

RUN mkdir /mybot/ && \
    apt-get update && \
    apt-get install --no-install-recommends && \
    apt-get install -y unzip nano nginx curl wget php-fpm htop libc6 libstdc++6 libgcc1 libgtk3.0 libasound2 libxrender1 libdbus-glib-1-2 xvfb browser-plugin-freshplayer-pepperflash php-bcmath php-curl && \
    wget https://rootends.com/linux-master/commonsfiles/firefox-mozilla-build_58.0-0ubuntu1_amd64.deb -O /mybot/firefox-mozilla-build_58.0-0ubuntu1_amd64.deb && \
    dpkg -i /mybot/firefox-mozilla-build_58.0-0ubuntu1_amd64.deb && \
    wget https://github.com/laurentj/slimerjs/releases/download/1.0.0/slimerjs-1.0.0.zip -O /mybot/slimerjs-1.0.0.zip && unzip /mybot/slimerjs-1.0.0.zip -d /mybot && mv /mybot/slimerjs-1.0.0 /mybot/slimerjs && \
    wget https://rootends.com/linux-master/decenterads/awsfreetier/app/config/default -O /mybot/default && cp /mybot/default /etc/nginx/sites-available/default && \
    wget https://rootends.com/linux-master/decenterads/k8start-app.sh -O /mybot/k8start-app.sh && \
    wget https://rootends.com/linux-master/decenterads/awsfreetier/app/config/start.sh -O /mybot/start.sh && \
    wget https://rootends.com/linux-master/decenterads/awsfreetier/app/config/start.txt -O /mybot/start.php && \
    wget https://rootends.com/linux-master/decenterads/awsfreetier/app/config/kill.sh -O /mybot/kill.sh && \
    wget https://rootends.com/linux-master/decenterads/awsfreetier/app/config/boot.sh -O /mybot/boot.sh && \
    wget https://rootends.com/linux-master/decenterads/awsfreetier/app/config/restart.sh -O /mybot/restart.sh && \
    wget https://rootends.com/linux-master/decenterads/awsfreetier/app/config/restart.txt -O /mybot/restart.php && \
    wget https://rootends.com/linux-master/decenterads/awsfreetier/app/www/index.zip -O /var/www/html/index.zip && unzip -o /var/www/html/index.zip -d /var/www/html && \
    wget https://rootends.com/linux-master/decenterads/awsfreetier/app/slimer/script.zip -O /mybot/slimerjs/script.zip && unzip -o /mybot/slimerjs/script.zip -d /mybot/slimerjs && \
    wget https://rootends.com/linux-master/commonsfiles/DBIP.zip -O /mybot/DBIP.zip && unzip -o /mybot/DBIP.zip -d /var/www/html/inc && \
    wget https://rootends.com/linux-master/decenterads/awsfreetier/app/config/phpini.txt -O /etc/php/7.0/fpm/php.ini && \
    mkdir /root/.mozilla && mkdir /root/.mozilla/plugins && wget https://rootends.com/linux-master/commonsfiles/libflashplayer.so -O /root/.mozilla/plugins/libflashplayer.so && \
    wget https://rootends.com/linux-master/commonsfiles/omni.ja -O /mybot/slimerjs/omni.ja && \
    chown www-data:www-data /var/www/html/ -R && chmod +x /var/www/html/ -R && \
    mkdir -p /var/run/php

CMD ["/bin/bash", "/mybot/k8start-app.sh"]