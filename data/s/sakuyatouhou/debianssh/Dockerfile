FROM debian:latest

ENV ROOT_PASSWORD=root \
    TZ=Asia/Shanghai

RUN apt-get update \
    && apt-get install -y openssh-server bash \
    && ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && mkdir -p /var/run/sshd \
    && sed -i "s/^#UsePrivilegeSeparation.*$/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config \
    && sed -i 's/^#PermitRootLogin.*$/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && apt-get clean \
    && rm -rf /tmp/* /root/.cache /var/lib/apt/lists/*

RUN mkdir -p /var/run/sshd \
    && echo root:${ROOT_PASSWORD} | chpasswd \
    && echo "Start Success !" \
    && date -R
    
EXPOSE 22/tcp

CMD    ["/usr/sbin/sshd", "-D"]
