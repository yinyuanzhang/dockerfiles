#
# Docker file to create an image that contains enough software to listen to events on the 433,92 Mhz band,
# filter these and publish them to a MQTT broker.
#
# The script resides in a volume and should be modified to meet your needs.
#
# Special attention is required to allow the container to access the USB device that is plugged into the host.
# The container needs priviliged access to /dev/bus/usb on the host.
# 
# docker run --name rtl_433 -d -e MQTT_HOST=<mqtt-broker.example.com> --privileged -v /dev/bus/usb:/dev/bus/usb  <image>

FROM alpine:3.9
MAINTAINER Korey Caro

LABEL Description="This image is used to start a script that will monitor for events on 433,92 Mhz"

# The script is in a volume. This makes changes persistent and allows you modify it.
VOLUME ["/scripts"]

WORKDIR /tmp

# First install software packages needed to compile rtl_433 and to publish MQTT events
RUN apk add --no-cache libusb-dev
RUN apk add --no-cache --virtual .build-deps build-base cmake git bash \

# Pull  source code from GIT, compile it and install it
  && git clone git://git.osmocom.org/rtl-sdr.git \
  && mkdir rtl-sdr/build \
  && cd rtl-sdr/build \
  && cmake ../ -DINSTALL_UDEV_RULES=ON -DDETACH_KERNEL_DRIVER=ON \
  && make  \
  && make install \
  
# Pull RTL_433 source code from GIT, compile it and install it
  && git clone https://github.com/merbanan/rtl_433.git \
  && cd rtl_433/ \
  && mkdir build \
  && cd build \
  && cmake ../ \
  && make \
  && make install \
  && cd / \
# Cleanup
  && rm -rf /tmp/rtl-sdr \
  && rm -rf /tmp/rtl_433 \
  && apk del .build-deps

# Define an environment variable
# Use this variable when creating a container to specify the MQTT broker host.
ENV MQTT_HOST=""

# When running a container this script will be executed
ENTRYPOINT ["/scripts/rtl2mqtt.sh"]

# Copy my script and make it executable
COPY rtl2mqtt.sh /scripts/rtl2mqtt.sh
RUN chmod +x /scripts/rtl2mqtt.sh
