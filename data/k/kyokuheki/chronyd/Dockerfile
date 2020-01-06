FROM alpine

# Volumes:
#  * /etc/chrony.conf - default configurtion file for chronyd
# Exposed ports:
#  * 123 - Network Time Protocol (NTP) - used for time synchronization
# Linux capabilities:
#  * SYS_TIME - Set system clock

LABEL MAINTAINER okd <kyokuheki@gmail.com>
LABEL build="docker build --tag=chrony ." \
      usage="docker run --net=host --cap-add SYS_TIME -d kyokuheki/chronyd"

RUN apk add --no-cache \
    chrony

EXPOSE 123 123/udp
VOLUME /etc/chrony.conf:/docker/chrony/chrony.conf
USER 0
CMD ["/usr/sbin/chronyd", "-d"]
