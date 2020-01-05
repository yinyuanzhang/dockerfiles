# 选择一个已有的os镜像作为基础  
FROM centos:centos7.6.1810

# 镜像的作者  
MAINTAINER author="nongbin"<1784855023@qq.com>

# 安装指定日常使用软件
RUN set -x \
&& yum install -y passwd \
&& yum install -y vim \
&& yum install -y wget \
&& yum install -y net-tools \
&& yum install -y unzip \
&& yum install -y tree \
&& yum install -y lrzsz \
&& yum install -y virt-what
 
# 指定root密码
RUN /bin/echo 'root:dockerdocker'|chpasswd

CMD ["/bin/bash"]