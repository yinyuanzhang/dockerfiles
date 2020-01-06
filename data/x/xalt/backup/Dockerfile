FROM ubuntu:18.04
MAINTAINER Philipp Goellner, philipp.goellner@xaltbc.de

ENV BACKUP_HOST                                    false
ENV BACKUP_KEY_FILE                                /tmp/id_rsa
ENV BACKUP_PATH                                    /backup/docker-applications
ENV BACKUP_USER                                    root
ENV BACKUP_SUFFIX                                  ""

ENV CRON_DATE                                      "0 0 * * *"

ENV DOCKER_COMPOSE_PULL                            false
ENV DOCKER_COMPOSE_VERSION                         1.23.2
ENV DOCKER_VERSION                                 18.03.1~ce-0~ubuntu

ENV DEBIAN_FRONTEND                                noninteractive

ENV SHELL                                          /bin/bash

ENV TIME_ZONE                                      false

RUN apt-get update -qq \ 
 && apt-get install --no-install-recommends -qq -y apt-transport-https \
                                                   ca-certificates \
                                                   cron \
                                                   curl \
                                                   gnupg \
                                                   jq \
                                                   openssh-client \
                                                   rsync \
                                                   software-properties-common \
                                                   tzdata \
 && curl -fsSL                                     https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
 && add-apt-repository                             "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable" \
 && apt-get update -qq \
 && apt-get install --no-install-recommends -qq -y docker-ce=${DOCKER_VERSION} \
 && rm -rf /var/lib/apt/lists/* \
 && curl -fsSL                                     https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose \
 && chmod 0755 /usr/local/bin/docker-compose

ADD configure-and-start-root.sh \
    backup.sh /

ENTRYPOINT ["/configure-and-start-root.sh"]
