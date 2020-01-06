#################################################################
## Poller Service
##
## @author peshkov@UDX
#################################################################

FROM        boxmls/node:v8

USER        root

RUN         \
            apt-get update && \
            apt-get install -y --force-yes openssh-server && \
            apt-get clean all

RUN         \
            mkdir /var/log/service-poller && \
            chown -R core:core /var/log/service-poller

RUN         mkdir -p /opt/sources/boxmls/service-poller

ADD         . /opt/sources/boxmls/service-poller/

RUN         \
            chmod +x /opt/sources/boxmls/service-poller/bin/* && \
            chown -R core:core /home/core && \
            chown -R core:core /opt/sources/boxmls/service-poller

WORKDIR     /opt/sources/boxmls/service-poller

USER        core

RUN         \
            cd /opt/sources/boxmls/service-poller && \
            npm install && \
            sudo npm link

ENTRYPOINT  [ "/bin/bash", "/opt/sources/boxmls/service-poller/bin/docker.entrypoint.sh" ]

CMD         [ "/bin/bash" ]
