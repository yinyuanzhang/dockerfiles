FROM ubuntu:18.04
MAINTAINER rectalogic

ENV container docker
ENV DEBIAN_FRONTEND=noninteractive
# Ensure UTF-8, or postgresql uses SQL_ASCII encoding
RUN echo "locales locales/default_environment_locale select en_US.UTF-8" | debconf-set-selections \
    && echo "locales locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8" | debconf-set-selections \
    && echo "tzdata tzdata/Areas select Etc" | debconf-set-selections \
    && echo "tzdata tzdata/Areas/Etc select UTC" | debconf-set-selections \
    && apt-get -y update \
    && apt-get -y install systemd openssh-client locales tzdata tmux ssh sudo dbus \
    && dpkg-reconfigure locales tzdata
ENV LANG=en_US.UTF-8

RUN systemctl set-default multi-user.target
RUN useradd -ms /bin/bash --groups sudo cureatr && echo 'cureatr:cureatr' | chpasswd && echo 'root:cureatr' | chpasswd
RUN echo cureatr | sudo --stdin bash -c "echo \"cureatr ALL=(ALL) NOPASSWD: ALL\" > /etc/sudoers.d/cureatr && chmod 0400 /etc/sudoers.d/cureatr"

COPY bootstrap-apt.sh /tmp
RUN /tmp/bootstrap-apt.sh

USER cureatr

RUN mkdir -p /home/cureatr/.ssh && ssh-keygen -q -t rsa -N '' -f /home/cureatr/.ssh/id_rsa && cp /home/cureatr/.ssh/id_rsa.pub /home/cureatr/.ssh/authorized_keys && chmod 0700 /home/cureatr/.ssh

COPY bootstrap-fab.sh pip-tools.txt requirements-bastion.txt /tmp/
RUN /usr/bin/python3.7 -m venv ~/env && bash -c "source ~/env/bin/activate && /tmp/bootstrap-fab.sh /tmp/pip-tools.txt /tmp/requirements-bastion.txt"
RUN ln -sfn /home/cureatr/dev/cureatr/server/dev/.bash_profile /home/cureatr/.bash_profile


# Now enable installed services to autostart, and cleanup
# http://askubuntu.com/questions/365911/why-the-services-do-not-start-at-installation
USER root
RUN rm -rf /usr/sbin/policy-rc.d /var/lib/apt/lists/* /tmp/bootstrap-fab.sh /tmp/bootstrap-apt.sh /tmp/pip-tools.txt /tmp/requirements-bastion.txt

WORKDIR /home/cureatr/dev

EXPOSE 22 27017 5001 5101 5102 5103 5104 8080

STOPSIGNAL SIGRTMIN+3
VOLUME ["/sys/fs/cgroup"]

ENTRYPOINT ["/sbin/init"]
