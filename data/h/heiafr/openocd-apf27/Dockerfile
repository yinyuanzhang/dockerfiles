# Embedded Systems - OpenOCD Docker file

FROM ubuntu:vivid
MAINTAINER Jacques Supcik "jacques.supcik@hefr.ch"

RUN apt-get update
RUN apt-get install -y openocd

ADD openocd/scripts/board/apf27.cfg    /usr/share/openocd/scripts/board/
ADD run_app.sh                         /usr/local/sbin/
RUN chmod +x /usr/local/sbin/run_app.sh

VOLUME /dev/bus/usb:/dev/bus/usb

CMD ["/bin/bash", "-c", "/usr/local/sbin/run_app.sh"]

EXPOSE 3333 4444 6666
