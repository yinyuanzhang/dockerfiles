#
# Builds a custom docker image for node-red and openhab
#
FROM nodered/node-red-docker

LABEL maintainer="MiGoller" \
      author="MiGoller" 

# Install additional "basic" nodes for openHAB
RUN npm install node-red-contrib-bigtimer
RUN npm install node-red-contrib-openhab2

# Define volume for Node-RED userdata: Settings, flows, ...
VOLUME ["/data"]
