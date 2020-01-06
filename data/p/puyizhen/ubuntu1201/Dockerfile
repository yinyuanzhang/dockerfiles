FROM       ubuntu:18.04
MAINTAINER puyizhen "puyizhen@gmail.com"

RUN apt-get update
RUN apt-get install -y openssh-server  python-pip libnet1 libnet1-dev libpcap0.8 libpcap0.8-dev nload htop fuse p7zip-full man-db git screen
RUN mkdir /var/run/sshd
RUN echo 'root:password' |chpasswd

RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
  
RUN pip install shadowsocks
RUN git clone https://github.com/snooda/net-speeder.git net-speeder
WORKDIR net-speeder
RUN sh build.sh
RUN mv net_speeder /usr/local/bin/
RUN chmod +x /usr/local/bin/net_speeder
COPY openssl.py /usr/local/lib/python2.7/dist-packages/shadowsocks/crypto/
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

RUN pip install requests
RUN pip install Pillow
RUN pip install scrapy
RUN mkdir /root/.ssh
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
# Configure container to run as an executable
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
EXPOSE 22
