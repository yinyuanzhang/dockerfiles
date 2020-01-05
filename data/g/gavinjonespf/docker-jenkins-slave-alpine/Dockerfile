FROM mhart/alpine-node:latest
ENV DOCKER_VERSION 17.05.0-ce
ENV DOCKER_COMPOSE_VERSION 1.13.0
ENV DOCKER_MACHINE_VERSION 0.7.0
ENV TERM xterm

RUN apk --update add openjdk7-jre openssh git curl && \
    rm -rf /var/cache/apk/* 

RUN addgroup jenkins && \
    adduser -D jenkins -s /bin/sh -G jenkins && \
    chown -R jenkins:jenkins /home/jenkins && \
    echo "jenkins:jenkins" | chpasswd

RUN ssh-keygen -A

#Docker bins
WORKDIR     /home/jenkins/
RUN         curl -L -o /tmp/docker-latest.tgz https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz && \
            tar -xvzf /tmp/docker-latest.tgz && \
            mv docker/* /usr/bin/ 

#Docker compose
RUN 		curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \
			chmod +x /usr/local/bin/docker-compose
  
RUN set -x && \
    echo "UsePrivilegeSeparation no" >> /etc/ssh/sshd_config && \
    echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "AllowGroups jenkins" >> /etc/ssh/sshd_config

# Comment these lines to disable sudo
RUN apk --update add sudo && \
    rm -rf /var/cache/apk/* && \
    echo "%jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

COPY ./init.sh /scripts/init.sh
RUN chmod 777 /scripts/init.sh
USER jenkins
RUN touch ~/.sudo_as_admin_successful
WORKDIR /home/jenkins

EXPOSE 22
CMD [ "/scripts/init.sh" ]
#CMD ["sudo", "/usr/sbin/sshd", "-D"]
