FROM lsiobase/ubuntu
MAINTAINER lassimus

RUN \
  echo "**** install shellinabox and openssl ****" && \
  apt-get update && \
  apt-get install -y \
          openssh-client \
          openssl \
          shellinabox && \
  echo "**** cleanup ****" && \
  apt-get clean && \
  rm -rf \
          /tmp/* \
          /var/lib/apt/lists/* \
          /var/tmp/*

# add local files
COPY root/ /

# Volumes and Ports
VOLUME /config
EXPOSE 4200
