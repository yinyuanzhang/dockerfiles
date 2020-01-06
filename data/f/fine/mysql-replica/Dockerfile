FROM mysql:5.7
ADD docker-entrypoint.sh /usr/local/bin
RUN \cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
