FROM ubuntu:16.04

ENV MQTT_HOST="localhost" \
    MQTT_PORT="1883" \
    MQTT_USER="" \
	MQTT_PASS="" \
	BASE_TOPIC="RTL_433" \
	USE_CHANNEL="no"

RUN apt-get update && apt-get install -y \
    rtl-sdr \
    librtlsdr-dev \
    librtlsdr0 \
    git \
    automake \
    libtool \
    cmake
	
RUN git clone https://github.com/merbanan/rtl_433.git \
  && cd rtl_433/ \
  && mkdir build \
  && cd build \
  && cmake ../ \
  && make \
  && make install

COPY rtl_433-mqtt.sh /scripts/rtl_433-mqtt.sh
RUN chmod +x /scripts/rtl_433-mqtt.sh
  
ENTRYPOINT ["/scripts/rtl_433-mqtt.sh"]