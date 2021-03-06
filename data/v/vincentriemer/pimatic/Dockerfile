##################################################################
# Dockerfile to create a PIMATIC container
# Tested and designed for Synology Diskstation but should run in all docker environments.
##################################################################

# We are using nodeJS as the base image
FROM node:7.6.0

# Author
MAINTAINER petschni

RUN apt-get update -y
RUN apt-get install -y libnss-mdns libavahi-compat-libdnssd-dev samba-common wakeonlan

####### PIMATIC installaton #######
RUN mkdir /home/pimatic-app
RUN /usr/bin/env node --version
RUN cd /home && npm install pimatic --prefix pimatic-app --production


####### Instal globally #######
RUN cd /home/pimatic-app/node_modules/pimatic && npm link

####### Copy the default config to our installation #######
RUN cp /home/pimatic-app/node_modules/pimatic/config_default.json /home/pimatic-app/config.json

####### Config the autostart #######
RUN wget https://raw.githubusercontent.com/pimatic/pimatic/v0.9.x/install/pimatic-init-d && cp pimatic-init-d /etc/init.d/pimatic
RUN chmod +x /etc/init.d/pimatic
RUN chown root:root /etc/init.d/pimatic
RUN update-rc.d pimatic defaults

####### Install pimatic-hap Correctly #######
RUN cd /home/pimatic-app/ && \
  npm install pimatic-hap && \
  cd node_modules/pimatic-hap && \
  npm install && \
  cd node_modules/hap-nodejs && \
  npm install

####### Copy entrypoint script to container #######
COPY entrypoint.sh /scripts/entrypoint.sh

####### Link the persistent config.json file and start the pimatic service #######
CMD ["bash", "/scripts/entrypoint.sh"]