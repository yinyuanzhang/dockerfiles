FROM alpine

MAINTAINER Chen Augus <tianhao.chen@gmail.com>

RUN apk update && apk add openldap openldap-back-bdb openldap-clients

RUN cp /etc/openldap/DB_CONFIG.example /var/lib/openldap/openldap-data/DB_CONFIG

EXPOSE 389 636

CMD ulimit -n 8192 && /usr/sbin/slapd -d 256
# 
# -u ldap -g ldap
