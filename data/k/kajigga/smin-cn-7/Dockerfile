FROM centos/systemd

ENV container docker

COPY ./ss.repo /etc/yum.repos.d/saltstack.repo

RUN rpm --import https://repo.saltstack.com/yum/redhat/7/x86_64/archive/2018.3.4/SALTSTACK-GPG-KEY.pub

RUN yum -q -y install salt-minion initscripts &&\
    yum clean all &&\
    systemctl enable salt-minion

VOLUME ["/etc/salt/minion.d", "/etc/salt/master.d"]

CMD ["/usr/sbin/init"]
