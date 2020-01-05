FROM ubuntu:18.04

LABEL license="MIT License"
LABEL maintainer="brian@bluerosedev.com"

ENV FOUNDATION_VERSION=5.2.5

RUN apt-get update \
    && apt-get install -y \
	    wget \
	    dpkg \
	    python \
	    net-tools \
	    lsb-base \
    && wget https://www.foundationdb.org/downloads/${FOUNDATION_VERSION}/ubuntu/installers/foundationdb-clients_${FOUNDATION_VERSION}-1_amd64.deb \
    && wget https://www.foundationdb.org/downloads/${FOUNDATION_VERSION}/ubuntu/installers/foundationdb-server_${FOUNDATION_VERSION}-1_amd64.deb \
    && dpkg -i foundationdb-clients_${FOUNDATION_VERSION}-1_amd64.deb \
    && dpkg -i foundationdb-server_${FOUNDATION_VERSION}-1_amd64.deb \
    && apt-get --purge remove -y wget

COPY start-foundationdb.sh /usr/bin/start-foundationdb.sh
COPY etc/init.d/foundationdb /etc/init.d/foundationdb

RUN chmod 755 /usr/bin/start-foundationdb.sh

ENTRYPOINT ["start-foundationdb.sh"]

EXPOSE 4500
