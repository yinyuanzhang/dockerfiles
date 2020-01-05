# 选择一个已有的os镜像作为基础  
FROM nongbin/centos7-bt.panel-ssh

# 镜像的作者  
MAINTAINER Author="nongbin" E-mila="1784855023@qq.com"

# 安装指定日常使用软件
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN yum install -y vim wget net-tools unzip tree lrzsz virt-what ntpdate iftop nethogs 

# 指定工作目录
ENV  MYPATH /root
WORKDIR $MYPATH

# 添加宝塔及ssh启动脚本并赋予执行权限
ADD dockerrun.sh /root
RUN chmod +x dockerrun.sh

# 清除历史命令及yum安装残留,这一步感觉无用功,算是给心里一个安慰而已
RUN history -cw 
RUN echo > /root/.bash_history 
RUN yum clean all

# 暴露端口
EXPOSE 20 21 22 443 80 888 8888 

# 执行dockerrun.sh脚本，开启ssh及宝塔服务
CMD ["/root/dockerrun.sh"]
