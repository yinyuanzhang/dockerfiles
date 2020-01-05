FROM centos:7

RUN yum -y install samba samba-client samba-common

RUN adduser --system shareuser

RUN chown -R shareuser /srv

COPY smb.conf /etc/samba/smb.conf

ENTRYPOINT /usr/sbin/smbd -FSD -d1 --option=workgroup=${workgroup:-workgroup}
