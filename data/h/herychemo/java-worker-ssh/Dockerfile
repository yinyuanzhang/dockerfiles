FROM openjdk:8-jre-stretch

RUN apt-get update

RUN apt install -y openssh-server \
	ssh

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN mkdir /home/worker

RUN useradd -d /home/worker -s /bin/bash -p "$(openssl passwd -1 workerPassword)" worker

USER worker
WORKDIR /home/worker


USER root

RUN mkdir /home/worker/.ssh
COPY /ssh-key/id_rsa.pub /id_rsa.pub
RUN cat /id_rsa.pub > /home/worker/.ssh/authorized_keys
RUN rm /id_rsa.pub

RUN chmod -R 700 /home/worker/.ssh
RUN chown -R worker:worker /home/worker

RUN systemctl enable ssh

RUN sed -i "s;PasswordAuthentication no;PasswordAuthentication yes;g" /etc/ssh/sshd_config
RUN sed -i "s;#PasswordAuthentication yes;PasswordAuthentication yes;g" /etc/ssh/sshd_config

RUN mkdir -p /var/run/sshd

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

