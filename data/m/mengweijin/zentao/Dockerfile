# 基础镜像
FROM centos:7
# 维护者信息
MAINTAINER Meng Wei Jin mengweijin.work@foxmail.com

ARG ZENTAO_NAME=zbox.tar.gz

# Linux 64位 一键安装包。Linux一键安装包必须直接解压到/opt目录下。
# ARG ZENTAO_URL=https://jaist.dl.sourceforge.net/project/zentao/10.5/ZenTaoPMS.10.5.stable.zbox_64.tar.gz
# Linux一键安装包64位（适用于Ubuntu17+，centos7.4+）
ARG ZENTAO_URL=http://dl.cnezsoft.com/zentao/11.6/ZenTaoPMS.11.6.stable.zbox_64.tar.gz

# 低版本Linux一键安装包64位（适用于ubuntu16及以下版本、centos7.3及以下版本）
# ARG ZENTAO_URL=http://dl.cnezsoft.com/zentao/11.6/ZenTaoPMS.11.6.stable.zbox_old.64.tar.gz

USER root
# 安装
RUN yum -y install wget && \
    # 下载禅道一键安装包到当前目录
    wget -O ${ZENTAO_NAME} ${ZENTAO_URL} && \
    # 解压
    tar -zxvf ${ZENTAO_NAME} -C /opt && \
    # 删除压缩包
    rm -f ${ZENTAO_NAME}

# 环境变量
ENV PATH /opt/zbox:$PATH

# 设置镜像时区为东八区时区，上海
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 添加挂载点	
VOLUME /opt/zbox

# apache服务器默认端口为80
EXPOSE 80

# tail -f /dev/null作用：必须存在一个一直运行的前台程序，否则容器启动后会自动停止
# ENTRYPOINT zbox start && tail -f /dev/null

# 以下来自nginx docker hub文档
# If you add a custom CMD in the Dockerfile, be sure to include -g daemon off; in the CMD in order for nginx to stay in the foreground, so that Docker can track the process properly (otherwise your container will stop immediately after starting)!
CMD zbox start -g 'daemon off;'