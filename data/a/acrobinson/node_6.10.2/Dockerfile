FROM centos
MAINTAINER Anthony Robinson

# deploy exists because bower doesn't like to run as root

RUN cd \
    && useradd deploy \
    && yum install -y epel-release \
    && yum install -y wget which git make bzip2 unzip fontconfig libicu libuv npm \
    && wget https://dl.yarnpkg.com/rpm/yarn.repo -O /etc/yum.repos.d/yarn.repo \
    && wget https://nodejs.org/dist/v6.10.2/node-v6.10.2-linux-x64.tar.gz \
    && tar -C /usr --strip-components 1 -xzf node-v6.10.2-linux-x64.tar.gz \
    && wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
    && tar -jxf phantomjs-2.1.1-linux-x86_64.tar.bz2 \
    && cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/sbin \
    && rm -rf phantomjs-2.1.1-linux-x86_64* \
    && rm -f node-v6.10.2-linux-x64.tar.gz \
    && yum install -y yarn \
    && npm install -g bower gulp \
    && curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "/tmp/awscli-bundle.zip" \
    && unzip /tmp/awscli-bundle.zip -d /tmp \
    && /tmp/awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws \
    && rm -f /tmp/awscli-bundle.zip \
    && rm -rf /tmp/awscli-bundle \
    && yum clean all
