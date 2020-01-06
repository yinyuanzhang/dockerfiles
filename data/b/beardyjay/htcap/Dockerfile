FROM debian:latest
MAINTAINER beardyjay <jay@beardyjay.co.uk>

WORKDIR /root
RUN apt-get update && apt-get -y install \
  bzip2 \
  git-core \
  python \
  sqlite3 \
  tar \
  wget \
&& rm -rf /var/lib/apt/lists/*

# Installing phantomJS
WORKDIR /root
RUN wget -q https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
    && tar -xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 \
    && mv /root/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/phantomjsa \
    && git clone https://github.com/segment-srl/htcap.git \
    && ln -s /usr/share/htcap/htcap.py /usr/local/bin/htcap \
    && ln -s /usr/share/htcap/scripts/htmlreport.py /usr/local/bin/htcap_report \
    && ln -s /usr/share/htcap/scripts/quickscan.sh /usr/local/bin/htcapquick

ENTRYPOINT ["htcap/htcap.py"]
