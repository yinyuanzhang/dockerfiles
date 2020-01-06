FROM mariadb:10.1
RUN echo "deb http://repos.um.ac.ir/ubuntu/ bionic main restricted universe multiverse" > /etc/apt/sources.list \
&&  echo "deb http://repos.um.ac.ir/ubuntu/ bionic-updates main restricted universe multiverse" >> /etc/apt/sources.list \
&&  echo "deb http://repos.um.ac.ir/ubuntu/ bionic-security main restricted universe multiverse" >> /etc/apt/sources.list
RUN apt-get -y update \
&&  apt-get -y install vim net-tools tcpdump psmisc dnsutils binutils
