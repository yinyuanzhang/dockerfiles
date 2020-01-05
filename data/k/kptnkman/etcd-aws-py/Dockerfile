# python image for build
FROM python:2.7.14-alpine

# setup my variables
ENV ETCD_CONFIG_FILE="/etc/etcd/etcd_config.yaml"
ENV ETCD_DATA_DIR="/var/lib/etcd"
ENV ETCD_CLIENT_PORT="2379"
ENV ETCD_SERVER_PORT="2380"
ENV ETCD_CLIENT_SCHEME="http"
ENV ETCD_PEER_SCHEME="http"
ENV CLOUD_PROVIDER="aws"
ENV ETCD_VER="3.2.24"
ENV ETCDCTL_API="3"

# set logging level: ERROR, WARNING, INFO, DEBUG, NOTSET
ENV LOGGING_LEVEL="DEBUG"

# Expose ports
EXPOSE ${ETCD_CLIENT_PORT}
EXPOSE ${ETCD_SERVER_PORT}

# Copy python requirements into image and run
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install depdencies needed to run
RUN apk --no-cache add \
    curl \
    bash \
    jq

# Create a /root/bin directory for our stuffs
RUN mkdir /etc/etcd

# Download and install etcd
RUN curl -L https://github.com/coreos/etcd/releases/download/v${ETCD_VER}/etcd-v${ETCD_VER}-linux-amd64.tar.gz -o etcd.tar.gz && \
    tar xzf etcd.tar.gz && \
    mv etcd-*/etcd etcd-*/etcdctl ./bin

# Expose volume for adding credentials
VOLUME ["/root/.aws"]

# Expose directory to write output to, and to potentially read certs from
VOLUME ["/etc/sysconfig/", "/etc/certs"]

# copy sample config from https://github.com/coreos/etcd/blob/master/etcd.conf.yml.sample
COPY etcd.conf.sample ./

# copy my app into image
COPY etcd-aws.py ./

# run my application
CMD python ./etcd-aws.py
