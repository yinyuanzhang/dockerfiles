FROM centos
MAINTAINER Anthony Robinson

RUN yum install -y epel-release \
    && yum install -y wget which git make bzip2 fontconfig npm unzip \
    && wget https://dl.yarnpkg.com/rpm/yarn.repo -O /etc/yum.repos.d/yarn.repo \
    && wget https://nodejs.org/dist/v6.2.2/node-v6.2.2-linux-x64.tar.gz \
    && tar -C /usr --strip-components 1 -xzf node-v6.2.2-linux-x64.tar.gz \
    && rm -f node-v6.2.2-linux-x64.tar.gz \
    && yum install -y yarn \
    && curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "/tmp/awscli-bundle.zip" \
    && unzip /tmp/awscli-bundle.zip -d /tmp \
    && /tmp/awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws \
    && rm -f /tmp/awscli-bundle.zip \
    && rm -rf /tmp/awscli-bundle \
    && npm cache clean \
    && yum clean all
