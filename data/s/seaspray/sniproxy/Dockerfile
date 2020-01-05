FROM ubuntu

RUN apt-get update && apt-get install -y git autotools-dev cdbs debhelper dh-autoreconf dpkg-dev gettext libev-dev libpcre3-dev libudns-dev pkg-config fakeroot devscripts

RUN git clone https://github.com/dlundquist/sniproxy.git
RUN cd sniproxy && ./autogen.sh 
RUN cd sniproxy && dpkg-buildpackage
RUN cd sniproxy && dpkg -i ../sniproxy_*.deb
COPY etc/sniproxy.conf /etc

ENTRYPOINT ["/usr/sbin/sniproxy","-f"]

EXPOSE 80 443

CMD ["-c", "/etc/sniproxy.conf"]
