# Clone from the CentOS 7
FROM seraus/whynot

MAINTAINER SA & OTHERS


ARG zeppelin_user=zeppelin_dock1
ENV env_zeppelin_user=$zeppelin_user

ENV container docker

ADD ipa-client-configure-first /usr/sbin/ipa-client-configure-first

RUN chmod -v +x /usr/bin/systemctl /usr/sbin/ipa-client-configure-first

ADD freeipa-install.service /etc/systemd/system/freeipa-install.service

RUN systemctl enable freeipa-install.service

VOLUME [ "/sys/fs/cgroup" ]

VOLUME ["/etc/security/keytabs"]

CMD ["/usr/sbin/init"]
