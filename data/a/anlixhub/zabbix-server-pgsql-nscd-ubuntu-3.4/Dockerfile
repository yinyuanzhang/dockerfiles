FROM zabbix/zabbix-server-pgsql:ubuntu-3.4-latest

RUN apt-get update && apt-get install -y nscd

ENTRYPOINT service nscd start && docker-entrypoint.sh
