FROM amazonlinux:latest

ENV DOCKER_VERSION 18.06.3
ENV DOCKER_COMPOSE_VERSION 1.24.0
ENV NGINX_VERSION 1.12

RUN yum install -y openssh-server sudo cronie tar git-core make && \
    systemctl enable crond.service && \
    sed -i 's/#\s*PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    ssh-keygen -q -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa && \
    ssh-keygen -q -f /etc/ssh/ssh_host_ecdsa_key -N '' -t ecdsa && \
    ssh-keygen -q -f /etc/ssh/ssh_host_ed25519_key -N '' -t ed25519 && \
    sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd && \
    systemctl enable sshd.service && \
    curl -fsSLO "https://download.docker.com/linux/static/stable/$(uname -m)/docker-${DOCKER_VERSION}-ce.tgz" && \
    tar xzvf docker-${DOCKER_VERSION}-ce.tgz --strip 1 -C /usr/local/bin docker/docker && \
    rm docker-${DOCKER_VERSION}-ce.tgz && \
    curl -fsSL "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" \
      -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose && \
    amazon-linux-extras install -y nginx$NGINX_VERSION && \
    systemctl enable nginx.service

RUN echo "DOCKER_HOST=tcp://docker:2375" >> /etc/environment

COPY ./users /users
RUN chmod +x /users/create-users.sh && \
    /users/create-users.sh docker && \
    rm /users/*.txt

CMD ["/usr/sbin/init"]
