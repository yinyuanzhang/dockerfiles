FROM solita/ubuntu-systemd

RUN apt update -y && apt upgrade -y

RUN apt install -y python2.7 python-pip python-dev libssh-dev sudo git aptitude software-properties-common

RUN apt-add-repository ppa:ansible/ansible \
    && apt update \
    && apt install -y ansible

RUN sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/'  /etc/sudoers

RUN mkdir -p /etc/ansible && echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts

VOLUME ["/sys/fs/cgroup"]

CMD ["/sbin/init"]