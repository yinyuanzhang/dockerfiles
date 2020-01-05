FROM debian:stretch

RUN apt-get update && apt-get -y upgrade && apt-get install -y apt-transport-https software-properties-common wget gnupg vim 
RUN wget -q -O- 'https://download.ceph.com/keys/release.asc' | apt-key add -
RUN apt-add-repository "deb https://download.ceph.com/debian-luminous/ $(lsb_release -sc) main"
RUN apt-get update && apt-get install -y ceph-common

ENTRYPOINT ["bash"]