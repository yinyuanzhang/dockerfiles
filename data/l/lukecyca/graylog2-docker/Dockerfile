FROM debian

RUN apt-get update

# Supervisord
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q supervisor && \
    mkdir -p /var/log/supervisor
CMD ["/usr/local/bin/graylog2-app"]

# SSHD
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q openssh-server && \
    mkdir /var/run/sshd && chmod 700 /var/run/sshd && \
    echo 'root:root' | chpasswd

# Utilities
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q vim curl wget ca-certificates apt-utils

# Install OpenJDK 7
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q openjdk-7-jre-headless

# MongoDB
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q pwgen && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
    echo 'deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen' > /etc/apt/sources.list.d/mongodb.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y -q mongodb-org-server

# ElasticSearch
RUN wget -q https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.90.10.tar.gz && \
    tar xf elasticsearch-*.tar.gz && \
    rm elasticsearch-*.tar.gz && \
    mv elasticsearch-* /opt/elasticsearch

# Graylog2 server
RUN wget  https://github.com/Graylog2/graylog2-server/releases/download/0.20.1/graylog2-server-0.20.1.tgz && \
    tar xzf graylog2-server-*.tgz && rm graylog2-server-*.tgz && \
    mv graylog2-server-* /opt/graylog2-server && \
    mkdir -p /opt/graylog2-server/plugins

# Graylog2 web interface
RUN wget  https://github.com/Graylog2/graylog2-web-interface/releases/download/0.20.1/graylog2-web-interface-0.20.1.tgz && \
    tar xzf graylog2-web-interface-*.tgz && rm graylog2-web-interface-*.tgz && \
    mv graylog2-web-interface-* /opt/graylog2-web-interface

# Configuration
ADD ./ /opt/graylog2-docker
RUN cd /opt/graylog2-docker && \
    cp graylog2.conf /etc/graylog2.conf && \
    sed -i -e "s/password_secret =$/password_secret = $(pwgen -s 96)/" /etc/graylog2.conf && \
    sed -i -e "s/root_password_sha2 =$/root_password_sha2 = $(echo -n admin | sha256sum | awk '{print $1}')/" /etc/graylog2.conf && \
    sed -i -e "s/application.secret=.*$/application.secret=\"$(pwgen -s 96)\"/" /opt/graylog2-web-interface/conf/graylog2-web-interface.conf && \
    sed -i -e "s/graylog2-server.uris=.*$/graylog2-server.uris=\"http:\/\/127.0.0.1:12900\/\"/" /opt/graylog2-web-interface/conf/graylog2-web-interface.conf && \
    echo "cluster.name: graylog2" >> /opt/elasticsearch/config/elasticsearch.yml && \
    cp supervisord-graylog.conf /etc/supervisor/conf.d

# Utility Shell Scripts
ADD run.sh /usr/local/bin/graylog2-app
ADD generate-configs.sh /usr/local/bin/generate-configs

# Expose ports
#   - 22: sshd
#   - 9000: Web interface
#   - 12201: GELF (UDP & TCP)
#   - 12900: REST API
EXPOSE 22 9000 12201 12201/udp 12900

# Expose data directories
VOLUME /opt/elasticsearch/data
VOLUME /opt/mongodb
