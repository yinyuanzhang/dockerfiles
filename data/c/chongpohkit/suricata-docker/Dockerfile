FROM ubuntu:18.04
#ENV container docker
## Install Suricata as describe here https://redmine.openinfosecfoundation.org/projects/suricata/wiki/CentOS_Installation
RUN apt-get update
RUN apt -y install libpcre3 libpcre3-dev build-essential autoconf wget apt-utils \
    automake libtool libpcap-dev libnet1-dev libyaml-0-2 libyaml-dev liblua5.1-dev \
    zlib1g zlib1g-dev libmagic-dev libcap-ng-dev libjansson-dev pkg-config \
    libnetfilter-queue-dev geoip-bin geoip-database geoipupdate apt-transport-https \
    clang libelf-dev software-properties-common apt-utils llvm-6.0-dev llvm-6.0 git-core

RUN ln -s /usr/lib/llvm-6.0/bin/llc /usr/bin/llc

COPY libbpf.tgz /tmp/
RUN cd /tmp/ && mkdir -p /usr/local/lib64/ && mkdir -p /usr/local/include/bpf && \
    tar -zxvf libbpf.tgz && cp /tmp/libbpf.a /usr/local/lib64/libbpf.a && cp /tmp/libbpf.so /usr/local/lib64/libbpf.so \
    && cp /tmp/libbpf.h /usr/local/include/bpf/libbpf.h && cp /tmp/bpf.h /usr/local/include/bpf/bpf.h \
    && echo "/usr/local/lib64/" >> /etc/ld.so.conf
RUN ldconfig

RUN ls -lrt /usr/bin/

#RUN cd /tmp/ \
#    && wget https://www.openinfosecfoundation.org/download/suricata-4.1.2.tar.gz \
#    && tar -xvzf /tmp/suricata-4.1.2.tar.gz 

RUN cd /tmp/ && git clone https://github.com/OISF/suricata.git \
    && cd suricata && git clone https://github.com/OISF/libhtp.git -b 0.5.x
RUN cd /tmp/suricata/ && ./autogen.sh && \
    CC=clang ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --enable-nfqueue --enable-lua \
    --disable-suricata-update --enable-ebpf --enable-ebpf-build
#RUN cd /tmp/suricata-4.1.2/ \
#    && CC=clang ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --enable-nfqueue --enable-lua \
#    --disable-suricata-update --enable-ebpf --enable-ebpf-build
#RUN cd /tmp/suricata-4.1.2/ebpf && cat Makefile
RUN cd /tmp/suricata/ \
    && make \
    && make install-full \
    && ldconfig
RUN cd /tmp/suricata/libhtp/ \
    && make install \
    && ldconfig
#RUN add-apt-repository ppa:oisf/suricata-stable
#RUN apt-get update
#RUN apt-get --yes --force-yes install suricata

# Install Suricata-update utility https://github.com/OISF/suricata-update
#RUN apt -y install python-pip python-yaml
#RUN pip install --pre --upgrade suricata-update

# Open up the permissions on /var/log/suricata so linked containers can
# see it.
RUN chmod 755 /var/log/suricata

COPY /Dockerfile/docker-entrypoint.sh /

VOLUME /var/log/suricata

RUN suricata -V

RUN suricata --build-info

ENTRYPOINT ["/docker-entrypoint.sh"]


#RUN apt install -y cronie
#COPY suricata-update.sh /etc/suricata/suricata-update.sh
# COPY file needed for the Suricata efficiency
#RUN apt install -y cronie
#COPY suricata-update-cron /etc/cron.d/suricata-update-cron
#RUN chmod +x /etc/cron.d/suricata-update-cron
#COPY docker-entrypoint.sh /tmp/docker-entrypoint.sh
#RUN chmod +x /tmp/docker-entrypoint.sh
#COPY suricata.yaml /etc/suricata/suricata.yaml


