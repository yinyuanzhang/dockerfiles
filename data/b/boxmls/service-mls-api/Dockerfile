#################################################################
## MLS API
##
#################################################################


FROM          boxmls/node:v8

USER          root

ENV           DOCKER_IMAGE boxmls/mls-api
ENV           NODE_PORT 8080
ENV           NODE_ENV production

RUN           \
              apt-get update && \
              apt-get install -y --force-yes openssh-server && \
              apt-get clean all

RUN           \
              chsh -s /bin/bash core

ADD           /. /opt/sources/boxmls/service-mls-api/

COPY          /static/etc/ssh.config /home/core/.ssh/config

RUN           ln -sf /opt/sources/boxmls/service-mls-api/static/git-hooks/post-merge.sh /opt/sources/boxmls/service-mls-api/.git/hooks/post-merge

RUN           \
              chmod +x /opt/sources/boxmls/service-mls-api/bin/*.sh && \
              chown -R core:core /opt/sources/boxmls/service-mls-api

RUN           \
              sudo chown -R core:core /home/core && \
              sudo chown -R core:core /opt/sources/boxmls/service-mls-api

RUN           \
              mkdir -p /var/log/service-mls-api && \
              touch /var/log/syslog && \
              sudo chown -R core:core /home/core/.ssh && \
              sudo chown -R core:core /var/log/service-mls-api && \
              sudo chown -R core:core /var/log/syslog

RUN           \
              echo "127.0.0.1 localhost" > /etc/hosts

WORKDIR       /opt/sources/boxmls/service-mls-api

EXPOSE        8080

USER          core

RUN           \
              ssh-keyscan -t rsa github.com | ssh-keygen -lf -

RUN           \
              cd /opt/sources/boxmls/service-mls-api && \
              NODE_ENV=production npm install && \
              sudo NODE_ENV=production npm link

ENTRYPOINT    [ "/bin/bash", "/opt/sources/boxmls/service-mls-api/bin/entrypoint.sh" ]


CMD           [ "/bin/bash" ]