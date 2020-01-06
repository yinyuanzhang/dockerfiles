# docker build --rm -t ophidia-all .

FROM indigodatacloud/centos-sshd:7
MAINTAINER Mario David <mariojmdavid@gmail.com>

RUN ansible-galaxy install indigo-dc.ophidia-all && \
    ansible-playbook /etc/ansible/roles/indigo-dc.ophidia-all/tests/test.yml

EXPOSE 22
CMD    ["/usr/sbin/sshd", "-D"]
