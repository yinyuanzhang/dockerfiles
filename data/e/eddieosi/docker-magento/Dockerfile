FROM bradfeehan/magento
# Based on bradfeehan/magento

MAINTAINER eddiosi docker@humanbyte.de

# Regenerate SSH host keys. This image does not contain any, so you
# have to do that yourself. You may also comment out this instruction;
# the init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh


# ...put your own build instructions here...

# /...


RUN apt-get update
RUN apt-get install wget -y
RUN apt-get install mysql-client mysql-common -y


# Clean up APT when done to save space
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# get magento
RUN cd /tmp && wget http://www.magentocommerce.com/downloads/assets/1.9.0.1/magento-1.9.0.1.tar.gz

# untar magento to /tmp
RUN cd /tmp && tar -zxvf magento-1.9.0.1.tar.gz


# remove default index.php from /app folder
RUN rm /app/index.php


# copy magento contents to /app folder
RUN cp -R /tmp/magento/* /app
RUN rm -R /tmp/magento/

RUN chmod -R o+w /app/media /app/var
RUN chmod o+w /app/app/etc && rm -f magento-*tar.gz

# add magento mage-cache.xml to configure the memcache
ADD magento/mage-cache.xml /app/app/etc/mage-cache.xml
ADD magento/start.sh /root/start.sh

RUN chmod +rwx /root/start.sh

EXPOSE 80

CMD ["/bin/sh", "/root/start.sh"]
