ARG target=amd64
FROM $target/debian:stretch

COPY qemu-* .dummy-qemu /usr/bin/

LABEL version="0.4" description="Mosquitto and OwnTracks Recorder"
LABEL authors="Jan-Piet Mens <jpmens@gmail.com>, Giovanni Angoli <juzam76@gmail.com>"

LABEL maintainer="Jesse Stuart <hi@jessestuart.com>"

ENV DEBIAN_FRONTEND noninteractive

ADD http://repo.owntracks.org/repo.owntracks.org.gpg.key /tmp/owntracks.gpg.key

RUN \
  apt-get update && \
  apt-get install -y gnupg && \
  apt-key add /tmp/owntracks.gpg.key && \
  apt-get update && \
  apt-get install -y software-properties-common net-tools && \
  apt-add-repository 'deb http://repo.owntracks.org/debian stretch main' && \
  apt-get update && \
  apt-get install -y \
    curl \
    libcurl3 \
    liblua5.2-0 \
    libmosquitto1 \
    libsodium18 \
    mosquitto \
    mosquitto-clients \
    ot-recorder \
    supervisor \
    && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# data volume
VOLUME /owntracks

COPY ot-recorder.default /etc/default/ot-recorder

COPY launcher.sh /usr/local/sbin/launcher.sh
COPY generate-CA.sh /usr/local/sbin/generate-CA.sh

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY mosquitto.conf mosquitto.acl /etc/mosquitto/

COPY recorder-health.sh /usr/local/sbin/recorder-health.sh
HEALTHCHECK CMD /usr/local/sbin/recorder-health.sh

RUN mkdir -p /var/log/supervisor && \
  mkdir -p -m 775 /owntracks/recorder/store && \
  chown -R owntracks:owntracks /owntracks && \
  chmod 755 /usr/local/sbin/launcher.sh /usr/local/sbin/generate-CA.sh /usr/local/sbin/recorder-health.sh

EXPOSE 1883 8883 8083
CMD ["/usr/local/sbin/launcher.sh"]
