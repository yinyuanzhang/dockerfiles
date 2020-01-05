FROM siwatinc/python3baseimage
ARG CACHEBUST=1
ENV ESPHOME_DASHBOARD_USE_PING="true"
RUN apt-get -y install iputils-ping
RUN pip install esphome
RUN pip install -U platformio
CMD esphome /config dashboard --password $password
