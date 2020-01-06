FROM ubuntu:18.04
MAINTAINER PR <docker@ongoing.today>

ENV DEBIAN_FRONTEND="noninteractive"

RUN apt -qq update && \
    apt install -yq --no-install-recommends \
        g++ \
        git \
        make \
        python-crypto \
        python-dpkt \
        python-ipy \
        python-pip \
        python-pypcap \
        wget && \
    pip install elasticsearch pygeoip && \
    git clone https://github.com/USArmyResearchLab/Dshell.git && \
    cd Dshell && \
    rm -rf .git && \
    make && \
    cd share/GeoIP && \
    wget https://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.tar.gz && \
    wget https://geolite.maxmind.com/download/geoip/database/GeoLite2-ASN.tar.gz && \
    tar xfz GeoLite2-Country.tar.gz && \
    tar xfz GeoLite2-ASN.tar.gz && \
    mv GeoLite2-Country*/GeoLite2-Country.mmdb . && \
    mv GeoLite2-ASN*/GeoLite2-ASN.mmdb . && \
    rm -rf GeoLite2-Country.tar.gz GeoLite2-ASN.tar.gz GeoLite2-Country_* GeoLite2-Country_* && \
    apt remove -yq g++ git make && \
    apt clean && apt autoclean && apt autoremove -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    mkdir -p /pcaps \

WORKDIR /pcaps

ENTRYPOINT ["/Dshell/dshell"]

