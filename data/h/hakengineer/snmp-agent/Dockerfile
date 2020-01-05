FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install -y \
    snmp snmpd \
    --no-install-recommends

RUN sed -ibak "s/mibs :/mibs all/" /etc/snmp/snmp.conf

RUN sed -ibak "s/agentAddress  udp:127.0.0.1:161/agentAddress  udp:161/" /etc/snmp/snmpd.conf && \
    sed -ibak "s/view   systemonly  included   .1.3.6.1.2.1.1/#view   systemonly  included   .1.3.6.1.2.1.1/" /etc/snmp/snmpd.conf && \
    sed -ibak "s/view   systemonly  included   .1.3.6.1.2.1.25.1/#view   systemonly  included   .1.3.6.1.2.1.25.1/" /etc/snmp/snmpd.conf && \
    sed -ibak "s/rocommunity public  default    -V systemonly/rocommunity public default/" /etc/snmp/snmpd.conf && \
    sed -ibak "s/rocommunity6 public  default   -V systemonly/#rocommunity6 public  default   -V systemonly/" /etc/snmp/snmpd.conf

EXPOSE 161/udp

ENTRYPOINT service snmpd start && bash
