FROM centos:centos7
MAINTAINER kvaps <kvapss@gmail.com>

ENTRYPOINT ["/bin/sh", "-c", "env > /etc/environment; exec /usr/sbin/init"]

ENV container docker

RUN find /etc/systemd/system/* '!' -name '*.wants' | xargs rm -rvf \
 && for i in basic.target sysinit.target network.service netconsole.service ; do rm -f /usr/lib/systemd/system/$i && ln -s /dev/null /usr/lib/systemd/system/$i ; done

ADD docker-container.target start.service /usr/lib/systemd/system/

RUN systemctl set-default docker-container.target \
 && systemctl enable start.service

ADD bin/ /bin/
ADD etc/ /etc/
