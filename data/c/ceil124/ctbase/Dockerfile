FROM centos:7.6.1810

ENV LANG=zh_CN.UTF-8 \
    LANGUAGE=zh_CN:zh \
    LC_ALL=zh_CN.UTF-8

RUN set -x \
  && yum install vim net-tools telnet curl bash-completion tree wget unzip deltarpm epel-release -y \
  && yum update -y \
  && yum install collectl htop -y \
  && yum clean all \
  && rm -rf /tmp/* rm -rf /var/cache/yum/* \
  && localedef -c -f UTF-8 -i zh_CN zh_CN.UTF-8 \
  && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

CMD ["bash"]