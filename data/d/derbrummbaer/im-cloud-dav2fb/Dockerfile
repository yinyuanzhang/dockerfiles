############################################################
# Dockerfile to build supervisor container image
# based on Ubuntu Xenial
############################################################
# Container Import Telefonbücher von Nextcloud zur FritzBox
############################################################

# Set the base Image
FROM derbrummbaer/im-base-phusion1604:test

# File Author / Maintainer
MAINTAINER Sven Berger

############################################################
# RUN INSTALL AS root
############################################################

USER root

############################################################
# Environment Variables
############################################################

ENV LC_ALL de_DE.UTF-8
ENV LANG de_DE.UTF-8
ENV LANGUAGE de_DE.UTF-8
ENV USERNAME ubuntu
ENV USERID 2000
ENV GROUPID 2000
ENV TZ Europe/Berlin

############################################################
# Container Users
############################################################

############################################################
# Update Repository and upgrade Software
############################################################

############################################################
# Konfigure timezone and locale
############################################################

############################################################
# Add Software Repositories
############################################################
RUN apt-get update; apt-get dist-upgrade -y

############################################################
# Begin Installation
############################################################
RUN apt-get install \
git \
php-cli \
php-curl \
php-ftp \
php-mbstring \
php-xml \
mc \
nano \
-y

############################################################
# Copy Files
############################################################
COPY ./my_init/* /etc/my_init.d/
RUN chmod +x /etc/my_init.d/*

COPY ./command/* /usr/local/bin/
RUN chmod +x /usr/local/bin/*

############################################################
# Remove Apt Data
############################################################
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

############################################################
# Container RUN USER
############################################################
#USER $USERNAME

############################################################
# Ports needed
############################################################

############################################################
# Ports needed by App
############################################################

############################################################
# Folders needed
############################################################
VOLUME /opt/carddav2fb

############################################################
# Container Start
############################################################
#ENTRYPOINT ["/usr/bin/php","/opt/carddav2fb/carddav2fb.php","/opt/carddav2fb/config.berger.php"]
#ENTRYPOINT ["/usr/bin/php","/opt/carddav2fb/carddav2fb.php"]
#CMD ["/opt/carddav2fb/run.sh"]
CMD ["/sbin/my_init"]
