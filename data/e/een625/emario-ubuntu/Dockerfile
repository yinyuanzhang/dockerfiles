FROM ubuntu
MAINTAINER Edward Mario (edward.mario@gmail.com)
RUN apt-get -y update && apt-get install -y openssh-server && apt-get install -y iputils-ping && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*
RUN useradd -m emario -s /bin/bash && usermod -aG sudo emario
RUN mkdir -p /home/emario/.ssh
COPY authorized_keys /home/emario/.ssh/authorized_keys
COPY sshd_config /etc/ssh/sshd_config
RUN chown emario:emario /home/emario/.ssh/authorized_keys && chmod 400 /home/emario/.ssh/authorized_keys
ENTRYPOINT /etc/init.d/ssh start && tail -f /dev/null
