FROM alpine/git:1.0.7
RUN mkdir /root/.ssh
COPY files/ssh.config /root/.ssh/config
COPY files/entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
