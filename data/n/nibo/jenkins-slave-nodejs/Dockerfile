FROM nibo/jenkins-slave:0.0.1
MAINTAINER Richard <nibocn@gmail.com>

ARG NODE_VERSION=v10.13.0

RUN \
    # Install tools
    yum makecache fast \
    && yum install -y git \
        \
    # Install Docker
    && yum install -y yum-utils \
    && yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo \
    && yum makecache fast \
    && yum install -y docker-ce \
        \
    # Install Nodejs
    && mkdir -p /opt/nodejs \
    && curl http://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}-linux-x64.tar.gz | tar -xzC /opt/nodejs --strip-components=1 \
    && ln -s /opt/nodejs/bin/* /usr/local/bin \
        \
    # Install nrm
    && npm install -g nrm \
    && ln -s /opt/nodejs/bin/nrm /usr/local/bin \
        \
    # Clean resource
    && yum clean all \
    && rm -rf /var/cache/yum/* \
    rm -rf /tmp/* \
    rm -rf /root/.npm/*

VOLUME /root/.npm

ENV LANG en_US.UTF-8
ENV NODEJS_HOME /opt/nodejs
ENV PATH $NODEJS_HOME/bin:$PATH

