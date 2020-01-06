FROM amazonlinux:2

ENV container docker

RUN yum makecache fast && yum update -y && \
    yum install -y python sudo yum-plugin-ovl bash initscripts systemd && \
    yum clean all && \
    (cd /lib/systemd/system/sysinit.target.wants/; for i in ; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done) && \
    rm -f /lib/systemd/system/multi-user.target.wants/* && \
    rm -f /etc/systemd/system/.wants/* && \
    rm -f /lib/systemd/system/local-fs.target.wants/* && \
    rm -f /lib/systemd/system/sockets.target.wants/udev && \
    rm -f /lib/systemd/system/sockets.target.wants/initctl && \
    rm -f /lib/systemd/system/basic.target.wants/* && \
    rm -f /lib/systemd/system/anaconda.target.wants/*

VOLUME [ "/sys/fs/cgroup" ]

ADD cmd.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/cmd.sh
CMD ["/usr/local/bin/cmd.sh"]
