#########################################
# MQTT broker: Mosquitto
# 1883
# Anonyme access
# No persistence
# V1.0 : Testing
#########################################
FROM alpine
MAINTAINER ouv27 <smo270970@hotmail.com>

# Install packages
RUN apk add --update mosquitto mosquitto-clients

# Expose MQTT port
EXPOSE 1883

ENTRYPOINT ["mosquitto"]