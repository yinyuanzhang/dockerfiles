FROM mysql:8
ADD docker-entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
RUN \cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
