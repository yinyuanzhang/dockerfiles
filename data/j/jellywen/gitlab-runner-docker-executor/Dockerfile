FROM centos:7.6.1810
MAINTAINER <wwenjiulong@163.com>

RUN yum update -y -q && \
yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo && \
yum install -y -q git yum-utils device-mapper-persistent-data lvm2 docker-ce && \

# nodejs
    curl --silent --location https://rpm.nodesource.com/setup_8.x | bash - && \
    yum -y install nodejs && \
    npm install forever -g && \
    npm install -g yarn && \
    npm install -g cnpm --registry=https://registry.npm.taobao.org