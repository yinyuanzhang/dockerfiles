FROM ukti/base-ubuntu

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get -y install strongswan iptables uuid-runtime \
    && rm -rf /var/lib/apt/lists/*

RUN rm /etc/ipsec.secrets

ADD  /root /

VOLUME /var/ipsec

# http://blogs.technet.com/b/rrasblog/archive/2006/06/14/which-ports-to-unblock-for-vpn-traffic-to-pass-through.aspx
EXPOSE 500/udp 4500/udp

CMD /usr/local/bin/start-vpn


ENV HOST vpn.example.com
