from jackadam/alpine_base
MAINTAINER jackadam<jackadam@sina.com>

RUN apk add openssh  &&\
    #修改root密码
    echo root:123456 | chpasswd && \
    #生成KEY
    ssh-keygen -q -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key -P '' -N '' &&\
    #允许远程登录
    sed -i "s/#PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config
	
#开放22端口
EXPOSE 22

CMD /usr/sbin/sshd -D
