FROM ubuntu:18.04

ENV DOCKER_PORT 22
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y install software-properties-common awscli jq ssh telnet curl groff less mysql-client \
   && apt-get clean && rm -rf /var/lib/apt/lists/*


# OpenSSH 
RUN sed -i s/#PermitRootLogin.*/PermitRootLogin\ no/ /etc/ssh/ssh_config \
    && sed -i s/#PermitUserEnvironment.*/PermitUserEnvironment\ yes/ /etc/ssh/ssh_config


RUN adduser -shell /bin/bash fargate
ADD environment /home/fargate/.ssh/environment
WORKDIR /home/fargate/

ADD participants/ /home/fargate/participants/
ADD sshadd /home/fargate/sshadd
ADD upsert /home/fargate/upsert
ADD route53data /home/fargate/upsert.json
RUN chmod +x /home/fargate/sshadd
RUN chmod +x /home/fargate/upsert
RUN mkdir -p /var/run/sshd
RUN /home/fargate/sshadd
ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ADD motd /etc/motd


EXPOSE $DOCKER_PORT

ENTRYPOINT ["/entrypoint.sh"]
