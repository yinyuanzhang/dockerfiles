#
# MAINTAINER        cucy <zhouru1991@vip.qq.com>
# Docker version 1.12.3
#
# Dockerizing CentOS7.2: Dockerfile for building CentOS images
##

# 基础镜像
FROM       centos:7.2.1511 
MAINTAINER cucy <zhouru1991@vip.qq.com>  # 谁创建，谁维护

# 环境变量可以写多个
ENV TZ "Asia/Shanghai"     
ENV TERM xterm

ADD aliyun-CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo
ADD yum.conf /etc/yum.conf
# add 文件也可以写多个， 这条命令是复制文件到 docker里边

ADD aliyun-epel.repo /etc/yum.repos.d/epel.repo 
# add命令比copy多两个功能 1.可以写http地址直接拷贝到容器里 2.可以自动解压文件到容器里

RUN yum install -y curl \
wget tar bzip2 unzip \
vim-enhanced passwd sudo yum-utils \
hostname net-tools rsync man  gcc gcc-c++ \
git make automake cmake patch logrotate \
python-devel libpng-devel libjpeg-devel  \
pwgen python-pip openssh-server telegraf && yum clean all

# run指令就是在linux里边里边执行
RUN mkdir /root/.pip 
ADD pip.conf /root/.pip/pip.conf

RUN pip install supervisor  && pip install --upgrade pip
ADD supervisord.conf /etc/supervisord.conf  
RUN mkdir -p /etc/supervisor.conf.d && \
    mkdir -p /var/log/supervisor 

EXPOSE 22  
# 暴露容器22号端口给宿主机

ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  
#  最后一条生效，每次都需要执行的命令，每次启动的时候.
