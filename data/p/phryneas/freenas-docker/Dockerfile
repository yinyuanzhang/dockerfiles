FROM ubuntu:16.04

RUN apt-get update -qq
RUN apt-get install -qy privoxy curl

RUN curl -s -o /tmp/adblock2privoxy_1.4.2_amd64.debian8.deb https://s3.amazonaws.com/ab2p/adblock2privoxy_1.4.2_amd64.debian8.deb
RUN dpkg -i /tmp/adblock2privoxy_1.4.2_amd64.debian8.deb
RUN cd /tmp; curl -s -O "https://easylist.to/easylist/easylist.txt"
RUN cd /tmp; curl -s -O "https://easylist.to/easylist/easyprivacy.txt"
RUN cd /tmp; curl -s -O "https://easylist.to/easylist/fanboy-annoyance.txt"
RUN cd /tmp; curl -s -O "https://easylist.to/easylistgermany/easylistgermany.txt"
RUN cd /tmp; curl -s -O "https://easylist-downloads.adblockplus.org/antiadblockfilters.txt"
RUN adblock2privoxy -p /etc/privoxy/ /tmp/easylist.txt /tmp/easyprivacy.txt /tmp/fanboy-annoyance.txt /tmp/easylistgermany.txt /tmp/antiadblockfilters.txt
#RUN adblock2privoxy -p /etc/privoxy/ "https://easylist.to/easylist/easylist.txt" "https://easylist.to/easylist/easyprivacy.txt" "https://easylist.to/easylist/fanboy-annoyance.txt" "https://easylist.to/easylistgermany/easylistgermany.txt" "https://easylist-downloads.adblockplus.org/antiadblockfilters.txt"

ADD ./privoxy-config /etc/privoxy/config
ADD ./run.sh /opt/
RUN chmod a+x /opt/run.sh

LABEL org.freenas.interactive="false" \
      org.freenas.version="0.1" \
      org.freenas.upgradeable="false" \
      org.freenas.expose-ports-at-host="true" \
      org.freenas.autostart="true" \
      org.freenas.port-mappings="8118:8118/tcp" \
      org.freenas.volumes="[]"

EXPOSE 8118

CMD ["/opt/run.sh"]
