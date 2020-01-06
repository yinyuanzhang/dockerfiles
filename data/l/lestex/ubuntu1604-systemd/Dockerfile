FROM ubuntu:16.04
LABEL maintainer Andrey Larin <lestex@gmail.com>
ENV container docker

# Don't start any optional services except for the few we need.
RUN find /etc/systemd/system \
         /lib/systemd/system \
         -path '*.wants/*' \
         -not -name '*journald*' \
         -not -name '*systemd-tmpfiles*' \
         -not -name '*systemd-user-sessions*' \
         -exec rm \{} \;

RUN systemctl set-default multi-user.target
VOLUME ["/sys/fs/cgroup"]

CMD ["/sbin/init"]
