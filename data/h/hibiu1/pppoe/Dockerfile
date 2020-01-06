FROM ubuntu:15.10
MAINTAINER hibiu1

# noninteractive mode
ENV \
  DEBIAN_FRONTEND=noninteractive

RUN \
  echo "Asia/Tokyo" > /etc/timezone && \
  locale-gen en_US.UTF-8 && \
  apt-get update && \
  apt-get install -y pppoe && \
  apt-get clean

# PPPoE configuration
# DNS server1,2 : 200.0.0.101, 200.0.0.102
# MTU : 1454 bytes
# proxyarp
#
# PPPoE user, password : pppoe-client, pppoe-client
# PPPoE Clinet IP : 200.0.0.240
RUN \
  sed -i -e "s/# ms-dns 192.168.1.1/ms-dns 200.0.0.101/" /etc/ppp/options && \
  sed -i -e "s/# ms-dns 192.168.1.2/ms-dns 200.0.0.102/" /etc/ppp/options && \
  sed -i -e "s/#mtu <n>/mtu 1454/" /etc/ppp/options && \
  sed -i -e "s/#proxyarp/proxyarp/" /etc/ppp/options && \
  echo "pppoe-client * \"pppoe-client\" 200.0.0.240" >> /etc/ppp/pap-secrets
