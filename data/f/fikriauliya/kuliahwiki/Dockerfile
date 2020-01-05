FROM simplyintricate/mediawiki
MAINTAINER Pahlevi Fikri Auliya "pahlevi.fikri.auliya@gmail.com"

ADD https://extdist.wmflabs.org/dist/extensions/Mantle-REL1_24-8fa4c6e.tar.gz /tmp/Mantle-REL1_24-8fa4c6e.tar.gz
ADD https://extdist.wmflabs.org/dist/extensions/MobileFrontend-REL1_24-011e6c1.tar.gz /tmp/MobileFrontend-REL1_24-011e6c1.tar.gz
ADD LocalSettings.php /usr/share/nginx/html/LocalSettings.php

RUN tar -xvzf /tmp/Mantle-REL1_24-8fa4c6e.tar.gz -C /usr/share/nginx/html/extensions/
RUN tar -xvzf /tmp/MobileFrontend-REL1_24-011e6c1.tar.gz -C /usr/share/nginx/html/extensions/

RUN chown -R www-data:www-data /usr/share/nginx/html/extensions/Mantle && rm /tmp/Mantle-REL1_24-8fa4c6e.tar.gz
RUN chown -R www-data:www-data /usr/share/nginx/html/extensions/MobileFrontend && rm /tmp/MobileFrontend-REL1_24-011e6c1.tar.gz