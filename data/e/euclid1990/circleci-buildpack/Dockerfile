FROM circleci/buildpack-deps:stretch

USER root

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y apt-utils gettext-base curl python3-pip && \
    apt-get clean && \
    rm -rf /var/cache/apt/* && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

RUN export VER="17.03.0-ce" && \
    curl -L -o /tmp/docker-$VER.tgz https://download.docker.com/linux/static/stable/x86_64/docker-$VER.tgz && \
    tar -xz -C /tmp -f /tmp/docker-$VER.tgz && \
    mv /tmp/docker/* /usr/bin

USER circleci

ENV PATH "$PATH:/home/circleci/.local/bin"

RUN mkdir -p $HOME/.ssh

RUN pip3 --no-cache-dir install awscli --upgrade --user

CMD ["/bin/sh"]
