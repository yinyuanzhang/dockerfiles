FROM phusion/baseimage:latest
ARG AMASS_VERSION=3.0.27
ENV PATH="/opt/amass_v${AMASS_VERSION}_linux_amd64:${PATH}"
RUN apt-get update
RUN apt-get -y install nmap build-essential flex bison git curl unzip
RUN curl -L https://github.com/OWASP/Amass/releases/download/v${AMASS_VERSION}/amass_v${AMASS_VERSION}_linux_amd64.zip \
> amass_v${AMASS_VERSION}_linux_amd64.zip && \
unzip amass_v${AMASS_VERSION}_linux_amd64.zip && \
rm amass_v${AMASS_VERSION}_linux_amd64.zip && \
mv amass_v${AMASS_VERSION}_linux_amd64 /opt
RUN git clone https://github.com/dneufeld/unicornscan.git
RUN curl https://raw.githubusercontent.com/SlackBuildsOrg/slackbuilds/master/network/unicornscan/patches/unicornscan-0.4.7-gcc5.patch > unicorn.patch
RUN patch unicornscan/src/unilib/tsc.c unicorn.patch
RUN cd unicornscan && ./configure CFLAGS=-D_GNU_SOURCE && make && make install
RUN curl https://raw.githubusercontent.com/superkojiman/onetwopunch/master/onetwopunch.sh > /usr/local/bin/onetwopunch.sh
RUN chmod 755 /usr/local/bin/onetwopunch.sh
RUN apt-get -y purge build-essential git curl unzip
RUN apt-get -y autoremove
