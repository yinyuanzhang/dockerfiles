FROM debian:jessie
ENTRYPOINT ["/usr/bin/ssh"]
RUN apt-get update \
    && apt-get install -y ssh \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get autoremove

RUN useradd -m -g ssh -d /home/ssh ssh
ADD ssh_config /etc/ssh/ssh_config
USER ssh
WORKDIR /home/ssh
RUN mkdir .ssh
