FROM centos:7

MAINTAINER Nikolaos Vyzas <pondix@gmail.com>

RUN echo -e "[proxysql_repo]\nname= ProxySQL YUM repository\nbaseurl=http://repo.proxysql.com/ProxySQL/proxysql-1.4.x/centos/\$releasever\ngpgcheck=1\ngpgkey=http://repo.proxysql.com/ProxySQL/repo_pub_key" > /etc/yum.repos.d/proxysql.repo && yum -y install proxysql-1.4.7 && mkdir /var/lib/proxysql && yum clean all

ENTRYPOINT ["proxysql", "-f", "-D", "/var/lib/proxysql"]
