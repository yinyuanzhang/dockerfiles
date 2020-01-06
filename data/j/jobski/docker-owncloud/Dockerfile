FROM l3iggs/lamp
MAINTAINER l3iggs <l3iggs@live.com>
# Report issues here: https://github.com/l3iggs/docker-owncloud/issues
# Say thanks by adding a star or a comment here: https://registry.hub.docker.com/u/l3iggs/owncloud/

# upldate package list
RUN pacman -Sy

# set environmnt variable defaults
ENV REGENERATE_SSL_CERT false
ENV START_APACHE true
ENV START_MYSQL true
ENV MAX_UPLOAD_SIZE 30G
ENV TARGET_SUBDIR oc

# remove info.php
RUN rm /srv/http/info.php

# to mount SAMBA shares: 
RUN pacman -S --noconfirm --needed smbclient

# install sudo
RUN pacman -S --noconfirm --needed sudo

# for video file previews
RUN pacman -S --noconfirm --needed ffmpeg

# for document previews
RUN pacman -S --noconfirm --needed libreoffice-fresh

# Install owncloud
RUN pacman -S --noconfirm --needed owncloud

# Install owncloud addons
RUN pacman -S --noconfirm --needed owncloud-app-bookmarks
RUN pacman -S --noconfirm --needed owncloud-app-calendar
RUN pacman -S --noconfirm --needed owncloud-app-contacts
RUN pacman -S --noconfirm --needed owncloud-app-documents
RUN pacman -S --noconfirm --needed owncloud-app-gallery

# enable large file uploads
RUN sed -i "s,php_value upload_max_filesize 513M,php_value upload_max_filesize ${MAX_UPLOAD_SIZE},g" /usr/share/webapps/owncloud/.htaccess
RUN sed -i "s,php_value post_max_size 513M,php_value post_max_size ${MAX_UPLOAD_SIZE},g" /usr/share/webapps/owncloud/.htaccess
RUN sed -i 's,<IfModule mod_php5.c>,<IfModule mod_php5.c>\nphp_value output_buffering Off,g' /usr/share/webapps/owncloud/.htaccess

# setup Apache for owncloud
RUN cp /etc/webapps/owncloud/apache.example.conf /etc/httpd/conf/extra/owncloud.conf
RUN sed -i '/<VirtualHost/,/<\/VirtualHost>/d' /etc/httpd/conf/extra/owncloud.conf
RUN sed -i 's,Alias /owncloud /usr/share/webapps/owncloud/,Alias /${TARGET_SUBDIR} /usr/share/webapps/owncloud/,g' /etc/httpd/conf/extra/owncloud.conf
RUN sed -i 's,Options Indexes FollowSymLinks,Options -Indexes +FollowSymLinks,g' /etc/httpd/conf/httpd.conf
RUN sed -i '$a Include conf/extra/owncloud.conf' /etc/httpd/conf/httpd.conf
RUN chown -R http:http /usr/share/webapps/owncloud/

# configure PHP open_basedir
RUN sed -i 's,^open_basedir.*$,\0:/usr/share/webapps/owncloud/:/usr/share/webapps/owncloud/config/:/etc/webapps/owncloud/config/,g' /etc/php/php.ini

# configure PHP enable POSIX
RUN sed -i 's/;extension=posix.so/extension=posix.so/g' /etc/php/php.ini

# configure PHP memory limit
RUN sed -i 's/memory_limit = 128M/memory_limit = 4096M/g' /etc/php/php.ini

# configure cron run
ADD cron.sh /root/cron.sh
RUN chmod +x /root/cron.sh

# configure loop run
ADD loop.sh /root/loop.sh
RUN chmod +x /root/loop.sh

# expose some important directories as volumes
#VOLUME ["/usr/share/webapps/owncloud/data"]
#VOLUME ["/etc/webapps/owncloud/config"]
#VOLUME ["/usr/share/webapps/owncloud/apps"]

# place your ssl cert files in here. name them server.key and server.crt
#VOLUME ["/https"]

# start servers using cron.sh
CMD ["/root/cron.sh"]
