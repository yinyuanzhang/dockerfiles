FROM telegraf

RUN echo "deb http://deb.debian.org/debian stable main non-free" > /etc/apt/sources.list \
 && apt-get update && apt-get install --no-install-recommends --assume-yes snmp-mibs-downloader \
 && download-mibs \
 && rm -rf /var/lib/apt/lists/*

