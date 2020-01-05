FROM debian:latest
LABEL Maintainer="hsin" Version="1.2" Password="123456" \
    Description="latest debian, install ssh and python" 

# 加速国内网络环境下载
#RUN sed -i -e "/security/s/^/#/" \
#    -e "s/deb.debian.org/mirrors.aliyun.com/g" /etc/apt/sources.list

RUN apt-get update && apt-get install -y \
    openssh-server python3 \
    && rm -rf /var/lib/apt/lists/*

# 添加 python3 软连接
RUN ln -s /usr/bin/python3 /usr/bin/python

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN mkdir /var/run/sshd 

RUN echo 'root:123456' | chpasswd

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

