FROM centos:centos7

RUN yum install -y passwd openssh openssh-server openssh-clients initscripts sudo

# LANG
RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8

## create user
RUN useradd docker
RUN passwd -f -u docker
RUN mkdir -p /home/docker/.ssh; chown docker /home/docker/.ssh; chmod 700 /home/docker/.ssh

## setup sudoers
RUN echo "docker    ALL=(ALL)       ALL" >> /etc/sudoers.d/docker

ADD run.sh /home/docker/run.sh
RUN chmod +x /home/docker/run.sh

## setup sshd and generate ssh-keys by init script
RUN /usr/sbin/sshd-keygen

RUN sed -ri 's/account    required     pam_nologin.so/#account    required     pam_nologin.so/' /etc/pam.d/login
RUN sed -ri 's/account    required     pam_nologin.so/#account    required     pam_nologin.so/' /etc/pam.d/sshd

EXPOSE 22
CMD ["/home/docker/run.sh"]
