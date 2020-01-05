# A containerized version of sendmail and cyrus imap intended to run as a mail server
#
# Version 1

# Pull from CentOS Image
FROM fedora:30

MAINTAINER john.brown@ost-linux.co.uk

LABEL "Description" "A containerized version of sendmail and cyrus imap intended to run as a mail server",
LABEL "Usage" "docker run -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v /tmp/$(mktemp -d):/run -e \"container=docker\""


RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

RUN yum install -y  \
	sed \
	make \
	sendmail \
	sendmail-cf \
	mailman \
	cyrus-imapd \
	cyrus-sasl-plain \
	patch \
	procps-ng
 
RUN yum clean all; systemctl enable sendmail.service ; systemctl enable cyrus-imapd.service; systemctl enable saslauthd.service

RUN yum -y install libnss-pgsql

COPY conf/nss-pgsql.conf /etc/
COPY conf/nss-pgsql-root.conf /etc/
COPY conf/nsswitch.conf /etc/
RUN chmod 600 /etc/nss-pgsql-root.conf
RUN chown root:root /etc/nss-pgsql-root.conf


ADD sendmail.cf /etc/mail/
ADD sendmail.mc /etc/mail/
ADD imapd.conf /etc/
ADD cyrus.conf /etc/
ADD runonce.service /etc/systemd/system/
ADD runonce /usr/local/sbin/

RUN chmod u+x /usr/local/sbin/runonce
RUN systemctl enable runonce

COPY ckuser_cyrus.m4 /usr/share/sendmail-cf/feature/
RUN sed -i "s/auth       required     pam_nologin.so//" /etc/pam.d/imap
RUN sed -i "s/auth       required     pam_nologin.so//" /etc/pam.d/sieve
RUN mkdir /var/milter; chown smmsp.smmsp /var/milter

#Backup the /etc/mail dir, so it can be unpacked so if it is volume mounted it wont be empty 

RUN tar czvf /root/etc_mail.tgz /etc/mail
RUN tar czvf /root/var_lib_imap.tgz /var/lib/imap


EXPOSE 25 587 465 993 143 4190
VOLUME ["/var/spool/imap", "/var/lib/imap", "/var/spool/mqueue", "/etc/mail", "/etc/pki/tls/certs/", "/sys/fs/cgroup", "/var/lib/mailman", "/home", "/var/milter" ]

CMD ["/usr/sbin/init"]
