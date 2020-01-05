#################################################################
##
## HHVM + NGINX + PAGESPEED + COMPOSER
##
#################################################################

FROM          hipstack/hipstack:0.2.0

USER          root

ENV           DOCKER_IMAGE boxmls/docker-hhvm-nginx

RUN						\
              wget -qO - https://packagecloud.io/gpg.key | sudo apt-key add -

RUN           \
              export DEBIAN_FRONTEND=noninteractive && \
              apt-get -y --force-yes update && \
              apt-get -y --force-yes upgrade

RUN           \
              export DEBIAN_FRONTEND=noninteractive && \
              apt-get -y --force-yes upgrade hhvm

ENV           NGINX_VERSION 1.9.4
ENV           NPS_VERSION 1.9.32.6

RUN           \
              echo deb http://httpredir.debian.org/debian wheezy-backports main | sudo tee /etc/apt/sources.list.d/backports.list && \
              apt-get update --fix-missing

RUN           \
              apt-get install -y --force-yes nginx && \
              apt-get clean all

RUN           \
              apt-get install -y --force-yes nginx-extras && \
              apt-get clean all

RUN           \
              cd /usr/src && \
              wget --quiet https://github.com/pagespeed/ngx_pagespeed/archive/release-1.9.32.6-beta.zip && \
              unzip release-1.9.32.6-beta.zip

RUN           \
              cd /usr/src/incubator-pagespeed-ngx-release-${NPS_VERSION}-beta/ && \
              wget --quiet https://dl.google.com/dl/page-speed/psol/${NPS_VERSION}.tar.gz && \
              tar -xzvf ${NPS_VERSION}.tar.gz && \
              rm -fv ${NPS_VERSION}.tar.gz

RUN           \
              cd /usr/src && \
              wget --quiet http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \
              tar -xvzf nginx-${NGINX_VERSION}.tar.gz && \
              cd /usr/src/nginx-${NGINX_VERSION}/ && \
                ./configure --add-module=/usr/src/incubator-pagespeed-ngx-release-${NPS_VERSION}-beta \
                  --with-http_ssl_module \
                  --with-threads \
                  --with-stream \
                  --prefix=/usr/local/share/nginx \
                  --conf-path=/etc/nginx/nginx.conf \
                  --sbin-path=/usr/sbin \
                  --error-log-path=/var/log/nginx/error.log && \
                  make && make install

RUN           \
              cd /usr && \
              rm -fr /usr/src/* && \
              mkdir -p /var/pagespeed/cache && \
              apt-get clean && \
              rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
              find /var/log -type f | while read f; do echo -ne '' > $f; done;

RUN           \
              curl -skS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin && \
              ln -sf /usr/local/bin/composer.phar /usr/local/bin/composer && \
              chmod +x /usr/local/bin/composer

RUN           \
              npm cache clean -f && \
              npm install -g n

RUN           n v8.16.0

RUN           \
              npm install -g npm@latest && \
              npm install -g pm2

RUN           \
              echo "127.0.0.1 localhost" >> /etc/hosts

EXPOSE        8000