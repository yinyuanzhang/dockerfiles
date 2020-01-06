FROM jenkinsci/jnlp-slave

USER root

ARG DOCKER_COMPOSE_VERSION=1.19.0
RUN cd /usr/local/bin \
    && curl -#L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` -o docker-compose \
    && chmod +x docker-compose

USER jenkins
