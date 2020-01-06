FROM ubuntu:xenial
MAINTAINER Florian Dubourg <fd@ingeteldata.fr>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y pkg-config
RUN apt-get install -y attr acl samba smbclient ldap-utils winbind libnss-winbind libpam-winbind krb5-user krb5-kdc supervisor
RUN apt-get install -y openvpn inetutils-ping
RUN rm -rf /var/lib/apt/lists/*
RUN mkdir -p /etc/samba/external /shares
ADD entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh
CMD ["bash","/entrypoint.sh","setup"]
