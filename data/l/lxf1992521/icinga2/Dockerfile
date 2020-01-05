FROM centos:7
RUN yum install -y openssl https://archive.fedoraproject.org/pub/fedora/linux/releases/30/Everything/x86_64/os/Packages/p/proxychains-ng-4.13-3.fc30.x86_64.rpm
RUN rpm -i https://packages.icinga.com/epel/icinga-rpm-release-7-latest.noarch.rpm && yum install -y icinga2-2.10.4 && rpm -e icinga-rpm-release
RUN yum install -y epel-release && yum install -y nagios-plugins-http nagios-plugins-mysql nagios-plugins-tcp && yum remove -y epel-release && yum clean all
RUN mkdir /run/icinga2 && chown icinga: /run/icinga2
COPY startup.sh /
ENTRYPOINT [ "bash", "/startup.sh" ]
