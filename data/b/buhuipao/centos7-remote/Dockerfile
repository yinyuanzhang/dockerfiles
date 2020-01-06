FROM centos

MAINTAINER buhuipao <chenhua22@outlook.com>

ENV GROUP buhuipao
ENV USER buhuipao
ENV PASSWORD buhuipao

COPY authorized_keys /root/authorized_keys

#安装sshd服务
RUN yum install password openssh-server -y &&\
    sed -ri 's/^UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config &&\
    ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key &&\
    ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key &&\
    ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key

#创建用户
RUN groupadd "$GROUP" &&\
    useradd -g "$GROUP" "$USER" -d /home/"$USER" &&\
    mkdir /home/"$USER"/.ssh &&\
    cp /root/authorized_keys /home/"$USER"/.ssh/authorized_keys &&\
    echo "${PASSWORD}" | passwd "$USER" --stdin &&\
    echo "${PASSWORD}" | passwd "root" --stdin

#安装xfce和x2go, NX协议比VNC更快速更安全
RUN yum install -y epel-release &&\
    yum groups install -y "xfce" &&\
    yum install -y x2goserver x2goserver-xsession

RUN sed -i "s/^#Port 22/Port 22/g" /etc/ssh/sshd_config &&\
    sed -i 's/^#PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config &&\
    sed -i 's/^#MaxAuthTries 6/MaxAuthTries 6/g' /etc/ssh/sshd_config &&\
    sed -i 's/^#RSAAuthentication yes/RSAAuthentication yes/g' /etc/ssh/sshd_config &&\
    sed -i 's/^#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config

EXPOSE 22

RUN /usr/sbin/sshd -D &

USER "$USER"

CMD ["startx"]
