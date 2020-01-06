FROM ubuntu:18.04

RUN find /etc/systemd/system \
     /lib/systemd/system \
     -path '*.wants/*' \
     -not -name '*journald*' \
     -not -name '*systemd-tmpfiles*' \
     -not -name '*systemd-user-sessions*' \
     -exec rm \{} \;

RUN apt -qq update && \
    apt -y install sudo software-properties-common \
    libvirt-bin systemd patch rsyslog udev && \
    systemctl set-default multi-user.target && \
    systemctl enable rsyslog.service && \
    apt clean all

RUN rsyslogd && \
    add-apt-repository ppa:maas/stable -y && \
    DEBIAN_FRONTEND=noninteractive apt install -y maas-cli maas-rack-controller && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    mv /usr/sbin/tcpdump /usr/bin/tcpdump && \
    ln -s /usr/bin/tcpdump /usr/sbin/tcpdump

COPY scripts/*.service /lib/systemd/system/
RUN systemctl enable register-rack-controller.service && \
    systemctl mask getty@tty1.service
    #mkdir -p /etc/systemd/system/basic.target.wants && \
    #ln -s /etc/systemd/system/journalctl-to-tty.service /etc/systemd/system/basic.target.wants/journalctl-to-tty.service

CMD ["/bin/bash", "-c", "exec /sbin/init --log-target=console 3>&1"]
