FROM nibo/java:8u171-jdk-fat
MAINTAINER Richard <nibocn@gmail.com>

ENV TZ=Asia/Shanghai

RUN yum makecache fast \
    && yum install -y openssh-server \
    && ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' \
    && echo "root:root" | chpasswd \
    && yum clean all \
    && rm -rf /var/cache/yum/*


VOLUME /opt/jenkins

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
