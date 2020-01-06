FROM alpine AS dl

ENV ARDUINO_VERSION=1.8.5
ENV ARDUINO_TAR=arduino-$ARDUINO_VERSION-linux64.tar.xz
ENV ARDUINO=/arduino

WORKDIR /
RUN \
	wget https://downloads.arduino.cc/$ARDUINO_TAR && \
	tar -xf $ARDUINO_TAR && \
	rm -rf $ARDUINO_TAR && \
	mv arduino-$ARDUINO_VERSION $ARDUINO

FROM debian:9.4
COPY --from=dl /arduino /arduino
