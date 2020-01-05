FROM jenkins:2.46.2

ARG docker_version=17.03.1-ce
USER root

RUN apt-get update \
    && apt-get install net-tools curl -y \
    && curl -fsSL https://get.docker.com/builds/Linux/x86_64/docker-${docker_version}.tgz -o /opt/docker-${docker_version}.tgz \
    && cd /opt \
    && tar -xzvf docker-${docker_version}.tgz \
    && chown -R jenkins ./docker/

ENV PATH "$PATH:/opt/docker/"
ENV DOCKER_HOST "tcp://dockerhost:2375"

COPY setup.sh /usr/local/bin/setup.sh
RUN chmod +x /usr/local/bin/setup.sh

ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/setup.sh"]
