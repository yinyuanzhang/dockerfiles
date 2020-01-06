FROM jsmitsnl/docker-openldap-postfix-book:latest
LABEL maintainer="gaetanlongree@gmail.com"

ADD default-structure.ldif /

VOLUME /var/lib/ldap
VOLUME /etc/ldap/slapd.d
VOLUME /container/service/slapd/assets/certs
