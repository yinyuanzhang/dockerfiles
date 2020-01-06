FROM ubuntu

COPY dist /root/dist
RUN apt update && \
    apt install -y openssh-server python2.7 && \
    ln -s /usr/bin/python2.7 /usr/bin/python && \
    rm -rf /var/cache/ && \
    rm /etc/ssh/sshd_config && \
    echo "root:root" | chpasswd && \
    mv /root/dist/sshd_config /etc/ssh/sshd_config && \
    mkdir /var/run/sshd && \
    mv /root/dist/*passwd /usr/local/sbin/ && \
    rm -rf /root/dist

CMD /usr/sbin/sshd -D
