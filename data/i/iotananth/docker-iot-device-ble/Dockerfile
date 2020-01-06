# Copyright 2016, Dell, Inc.
# Docker image for Dell Fuse Command micro service 
FROM java:8
MAINTAINER Anantha Boyapalle <anantha_boyapalle@dell.com>

# environment variables
ENV APP_DIR=/dell-iot/iot-device-ble
ENV APP=iot-device-ble.jar
ENV APP_PORT=9992

#copy JAR and property files to the image
COPY *.jar $APP_DIR/$APP
COPY *.properties $APP_DIR/

EXPOSE $APP_PORT

#set the working directory
WORKDIR $APP_DIR

#kick off the micro service
ENTRYPOINT java -jar $APP

