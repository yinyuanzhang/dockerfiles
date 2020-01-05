FROM centos
MAINTAINER Anthony Robinson

# deploy exists because bower doesn't like to run as root

RUN cd \
    && useradd deploy \
    && yum install -y epel-release \
    && yum install -y wget npm which git make bzip2 fontconfig \
    && yum clean all \
    && wget https://nodejs.org/dist/v4.3.0/node-v4.3.0-linux-x64.tar.gz \
    && tar -C /usr --strip-components 1 -xzf node-v4.3.0-linux-x64.tar.gz \
    && wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
    && tar -jxf phantomjs-2.1.1-linux-x86_64.tar.bz2 \
    && cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/sbin \
    && rm -rf phantomjs-2.1.1-linux-x86_64* \
    && rm -f node-v4.3.0-linux-x64.tar.gz \
    && npm install -g npm \
    && npm install -g bower gulp \
    && npm cache clean
