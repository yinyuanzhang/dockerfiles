#zabbix-appliance docker-container for general purpose:
#build with docker build -f zabbix-appliance.docker -t fugitivus/zabbix:latest .
#docker run --name zabbix --hostname zabbix -p 80:80 -p 10051:10051 -d fugitivus/zabbix-appliance

FROM zabbix/zabbix-appliance:ubuntu-latest
MAINTAINER fugitivus <fugitivus@gmx.de>

#environment-variables for non-interactive shell:
#ENV DEBIAN_FRONTEND noninteractive

#install updates, some packages and do cleanup:
RUN apt-get update && apt-get upgrade -y\
#RUN apt-get update\
 && apt-get install apt-utils inetutils-ping fping joe net-tools -y\
 && chown root:zabbix /usr/bin/fping\
 && chmod 4710 /usr/bin/fping\
 && apt-get clean autoclean\
 && apt-get autoremove -y\
 && rm -rf /var/lib/{apt,dpkg,cache,log}/
#ENTRYPOINT ["docker-entrypoint.sh"]
