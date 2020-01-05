FROM centos:latest
MAINTAINER Daniel Shaffer <dasbeta@gmail.com>

WORKDIR /root
RUN yum install -y wget
RUN wget http://download.silicondust.com/hdhomerun/hdhomerun_record_linux
ADD hdhomerun /etc/rc.d/
ADD hdhomerun.conf /root
ADD upgrade_hdhomerun.sh /root
RUN chmod u+x hdhomerun_record_linux
RUN chmod +x /etc/rc.d/hdhomerun
RUN chmod u+x /root/upgrade_hdhomerun.sh
RUN echo "hdhomerun_enable=\"YES\"" >> /etc/rc.conf

LABEL org.freenas.version="0.21" \
      org.freenas.autostart="true" \
      org.freenas.bridged="true" \
      org.freenas.dhcp="false" \
#      org.freenas.expose-ports-at-host="true" \
      org.freenas.interactive="false" \
      org.freenas.port-mappings="65001:65001/udp,65002:65002/tcp" \
#      org.freenas.settings="[]" \
#      org.freenas.static-volumes="[]" \
      org.freenas.upgradeable="false" \
      org.freenas.volumes="[ \
          { \
              \"name\": \"/mnt/recordings\", \
              \"descr\": \"Recordings Directory\" \
          } \
      ]"
#      org.freenas.web-ui-path="" \
#      org.freenas.web-ui-port="" \
#      org.freenas.web-ui-protocol=""
