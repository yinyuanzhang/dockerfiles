FROM ubuntu:18.04
RUN apt update -y
RUN apt install gpg apt-transport-https curl -y
RUN echo "deb https://deb.torproject.org/torproject.org/ bionic main" > /etc/apt/sources.list.d/tor.list
RUN curl https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | gpg --import
RUN gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | apt-key add -
RUN apt update -y
RUN apt upgrade -y
RUN apt install tor obfs4proxy tor-geoipdb torsocks deb.torproject.org-keyring -y
CMD service tor stop
COPY torrc /etc/tor/
COPY torsocks.conf /etc/tor/
ENTRYPOINT /usr/sbin/tor
