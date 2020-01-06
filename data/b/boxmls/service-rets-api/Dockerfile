#################################################################
## MPO RETS API
##
##
## @author potanin@UD
#################################################################

FROM          boxmls/hhvm-nginx:latest

USER          root

ENV           DOCKER_IMAGE boxmls/rets-api
ENV           NODE_PORT 3000
ENV           HOME /home/core

RUN           rm -rf /etc/apt/sources.list.d/*

RUN           apt-get update && \
              apt-get install -y --force-yes openssh-server && \
              apt-get clean all

RUN           \
              usermod --home /home/core --login core hipstack && \
              usermod -a -G sudo core && \
              groupmod -n core hipstack && \
              echo core:jxchpwnzaggbyhme | /usr/sbin/chpasswd && \
              usermod -a -G sudo core && \
              mv /home/hipstack /home/core && \
              yes | cp -r /root/.scripts /home/core && \
              chown -R core:core /home/core && \
              echo "core ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

RUN           \
              mkdir /var/log/service-rets-api && \
              chown 500:500 /var/log/service-rets-api

ADD           . /opt/sources/boxmls/service-rets-api/

WORKDIR       /opt/sources/boxmls/service-rets-api

RUN           \
              ln -sf /opt/sources/boxmls/service-rets-api/static/etc/default/hhvm.sh /etc/default/hhvm.sh && \
              ln -sf /opt/sources/boxmls/service-rets-api/static/etc/hhvm/php.ini /etc/hhvm/php.ini && \
              ln -sf /opt/sources/boxmls/service-rets-api/static/etc/hhvm/server.ini /etc/hhvm/server.ini && \
              ln -sf /opt/sources/boxmls/service-rets-api/static/etc/nginx/default.conf /etc/nginx/sites-enabled/default && \
              ln -sf /opt/sources/boxmls/service-rets-api/static/etc/nginx/nginx.conf /etc/nginx/nginx.conf && \
              ln -sf /opt/sources/boxmls/service-rets-api/static/etc/home/bashrc.sh /home/core/.bashrc

RUN           \
              chmod +x /opt/sources/boxmls/service-rets-api/bin/*.sh && \
              chmod +x /opt/sources/boxmls/service-rets-api/static/etc/home/bashrc.sh && \
              chown -R 500:500 /opt/sources/boxmls/service-rets-api

RUN           \
              touch /var/log/syslog && \
              sudo chown -R 500:500 /var/log/syslog

RUN           \
              sudo chown -R 500:500 /home/core && \
              sudo chown -R 500:500 /etc/hhvm && \
              sudo chown -R 500:500 /opt/sources/boxmls/service-rets-api && \
              sudo chown -R core:core /usr/local/bin

RUN           npm install

HEALTHCHECK   --interval=5s --timeout=3s CMD curl -f http://localhost:80/ping || exit 1

VOLUME        [ "/opt/sources/boxmls/service-rets-api" ]

EXPOSE        80

USER          core

ENTRYPOINT    [ "/bin/bash", "/opt/sources/boxmls/service-rets-api/bin/docker.entrypoint.sh" ]

CMD           [ "/bin/bash" ]