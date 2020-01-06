FROM ubuntu:18.04

LABEL maintainer="bitbucket@bebef.de" \
      version="3.2.1" \
      description="Provides TP-Link's Omada Controller Software in a docker container."

COPY --chown=508:508 *.sh /opt/tplink/EAPController/

# install runtime dependencies
RUN export DEBIAN_FRONTEND=noninteractive && \
  apt-get -qq update && \
  apt-get -y full-upgrade && \
  apt-get -qq install \
    libcap-dev \
    net-tools \
    unzip \
    wget && \
  rm -rf /var/lib/apt/lists/*

# install omada controller (instructions taken from install.sh); then create a user & group and set the appropriate file system permissions
RUN cd /tmp && \
  mkdir Omada && \
  cd Omada && \
  wget --quiet https://static.tp-link.com/2019/201907/20190726/Omada_Controller_v3.2.1_linux_x64.tar.gz && \
  tar xzf *.tar.gz && \
  cd $(find . -maxdepth 1 -type d -name 'Omada*') && \
  cd $(find . -maxdepth 1 -type d -name 'Omada*') && \
  cp -r * /opt/tplink/EAPController/ && \
  cd /tmp && \
  rm -rf Omada && \
  groupadd -g 508 omada && \
  useradd -u 508 -g 508 -d /opt/tplink/EAPController omada && \
  mkdir /opt/tplink/EAPController/logs /opt/tplink/EAPController/work && \
  chown -R omada:omada /opt/tplink/EAPController && \
  chmod a+x /opt/tplink/EAPController/bin/* && \
  chmod a+x /opt/tplink/EAPController/jre/bin/*

USER omada
WORKDIR /opt/tplink/EAPController
EXPOSE 8043 27001/udp 29810/udp 29811 29812
VOLUME ["/opt/tplink/EAPController/data","/opt/tplink/EAPController/work","/opt/tplink/EAPController/logs"]
ENTRYPOINT ["/opt/tplink/EAPController/entrypoint.sh"]
HEALTHCHECK --start-period=120s --timeout=10s CMD /opt/tplink/EAPController/healthcheck.sh
