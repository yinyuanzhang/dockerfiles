FROM ubuntu:bionic-20181018

ENV LANG=C.UTF-8 TZ=Asia/Shanghai

RUN apt update &&\
    DEBIAN_FRONTEND=noninteractive apt install -y net-tools expect unzip openssh-server openssh-sftp-server lftp rsync curl wget git sshpass --no-install-recommends &&\
    apt autoremove -y && apt clean && rm -rf /var/lib/apt/lists* /tmp/* /var/tmp/*

RUN ssh-keygen -A &&\
    ssh-keygen -t rsa -f ~/.ssh/id_rsa -N '' &&\
    cat ~/.ssh/id_rsa.pub > ~/.ssh/authorized_keys &&\
    chmod 600 ~/.ssh/authorized_keys &&\
    echo 'root:root' | chpasswd &&\
    echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config &&\
    echo 'StrictHostKeyChecking no' >> /etc/ssh/ssh_config &&\
    mkdir /run/sshd

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D", "-e"]