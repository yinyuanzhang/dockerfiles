FROM python:3.6.9

LABEL maintainer "mats116 <mats.kazuki@gmail.com>"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y lsb-release && \
    # App Engine SDK
    echo "deb http://packages.cloud.google.com/apt cloud-sdk-jessie main" > /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update && \
    apt-get install -y google-cloud-sdk-app-engine-python && \
    # Cloud SQL Proxy
    wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O /usr/local/bin/cloud_sql_proxy && \
    chmod +x /usr/local/bin/cloud_sql_proxy && \
    # MySQL Client 5.7
    export DEBIAN_FRONTEND=noninteractive && \
    wget http://repo.mysql.com/mysql-apt-config_0.8.13-1_all.deb -O /tmp/mysql-apt-config.deb && \
    dpkg -i /tmp/mysql-apt-config.deb && \
    apt-get update && \
    apt-get install -y --allow-unauthenticated mysql-community-client=8.0.* && \
    rm -f /tmp/mysql-apt-config.deb

CMD ["/bin/bash"]
