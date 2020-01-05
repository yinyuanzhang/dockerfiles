FROM arm32v7/python:2.7-alpine
COPY qemu-arm-static /usr/bin
LABEL maintainer="tanguy+github@baudrin.fr"
ENV PYTHONIOENCODING="UTF-8"

RUN /usr/bin/qemu-arm-static /bin/sh -c "apk add git mediainfo nodejs unrar tzdata" 

RUN /usr/bin/qemu-arm-static /bin/sh -c  "mkdir /app /var/run/sickchill /data /downloads /tv"

WORKDIR /app/sickchill

CMD /usr/local/bin/python SickBeard.py -q --nolaunch --datadir=/data --port 8081

COPY . /app/sickchill
