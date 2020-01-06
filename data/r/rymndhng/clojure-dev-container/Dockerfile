FROM openjdk:8u131-jdk-alpine

RUN apk update
RUN apk add git openrc jq py-pip postgresql curl
RUN pip install awscli

# Install postgres
RUN apk add postgresql && \
    rc-update add postgresql && \
    rc-status && \
    touch /run/openrc/softlevel && \
    /etc/init.d/postgresql start && \
    /etc/init.d/postgresql stop

# install leiningen, taken from juxt/docker
ENV LEIN_ROOT 1
RUN apk add --update wget ca-certificates bash && \
    wget -q "https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein" \
         -O /usr/local/bin/lein && \
    chmod 0755 /usr/local/bin/lein && \
    lein && \
    apk del wget ca-certificates && \
    rm -rf /tmp/* /var/cache/apk/*

# install Yopa
COPY yopa /opt/yopa
RUN /opt/yopa/configure.sh
ADD https://github.com/unbounce/yopa/releases/download/1.0.0-SNAPSHOT/yopa-1.0.0-SNAPSHOT-standalone.jar /opt/yopa/yopa-1.0.0-SNAPSHOT-standalone.jar
RUN chmod 644 /opt/yopa/yopa-1.0.0-SNAPSHOT-standalone.jar

# install mysql
RUN apk add --update mysql mysql-client && \
    rc-update add mariadb && \
    rc-status && \
    touch /run/openrc/softlevel && \
    /etc/init.d/mariadb setup && \
    /etc/init.d/mariadb start && \
    /usr/bin/mysqladmin -u root password 'root' && \
    /etc/init.d/mariadb stop
