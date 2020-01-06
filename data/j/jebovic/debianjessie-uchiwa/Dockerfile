FROM debian:jessie

MAINTAINER Jérémy Baumgarth

ENV DEBIAN_FRONTEND noninteractive

# Install stuff
RUN apt-get update \
    && apt-get install -y --no-install-recommends wget ca-certificates apt-transport-https

# Install Sensu from sensu apt repository
RUN wget -q https://sensu.global.ssl.fastly.net/apt/pubkey.gpg -O- | apt-key add - \
    && echo "deb https://sensu.global.ssl.fastly.net/apt jessie main" >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends uchiwa \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

# Uninstall stuff
RUN apt-get remove -y wget  ca-certificates apt-transport-https \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

# Configure sensu
RUN mkdir -p /etc/sensu
COPY config/uchiwa.json /etc/sensu/uchiwa.json

# init script
COPY init_script.sh /init_script.sh
RUN chmod +x /init_script.sh

CMD ["/bin/sh", "/init_script.sh"]

