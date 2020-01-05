# 选择一个已有的os镜像作为基础  
FROM centos:centos7.6.1810

# 镜像的作者  
MAINTAINER Author="nongbin" E-mila="1784855023@qq.com"

# 安装日常需要命令，安装shellinabox网页终端
RUN set -x \
&& yum install -y passwd net-tolls lrzsz coreutils
# 开始安装shellinabox ,
# 创建文件夹
RUN mkdir /opt/soft && \
#  进入文件夹
cd /opt/soft && \
# 安装基本工具
yum install -y vim lrzsz openssl gcc gcc-c++ make git && \
#  git克隆shellinabox
git clone https://github.com/SoulSu/shellinabox.git && \
# 进入目录查看文件
cd shellinabox && \
#  编译文件
./configure && \
# 安装
make && make install

# 设置root密码以及添加docker用户，并将docker用户加入sudoers文件
RUN set -x \
&& echo -e "root:docker"|chpasswd \
&& useradd docker \
&& echo -e "docker:dockerdocker"|chpasswd \
&& echo -e "docker ALL=(ALL)  ALL" >> /etc/sudoers 

# 指定工作目录
ENV  MYPATH /root
WORKDIR $MYPATH

# 添加后台挂载启动脚本并赋予执行权限
ADD bootup.sh /root
RUN chmod +x bootup.sh

# 清除历史命令及yum安装残留
RUN history -cw 
RUN echo > /root/.bash_history 
RUN yum clean all

# 暴露端口
EXPOSE 9999

# 执行bootup.sh脚本，开启shellinabox服务
CMD ["/root/bootup.sh"]
