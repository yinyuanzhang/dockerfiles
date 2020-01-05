FROM centos:6

RUN \
	set -x &&\
	yum -y install gcc httpd php php-pdo php-devel yum-utils
RUN \
	set -x &&\
	cd /etc/yum.repos.d/ &&\
	awk 'BEGIN{getline <"/etc/redhat-release";ver=gensub(".*([0-9]+\\.[0-9]+).*", "\\1", "");}/extras|contrib|centosplus/{exit;}/6\.1/{exit;}{gsub("6\\.0", ver);}/^\[/{sub("\\]", "-src]");}/^name/{$0=$0" - src";}/^baseurl/{sub("\\$basearch", "Source");}/^enabled/{sub("0", "1");}{print;}' CentOS-Vault.repo >CentOS-src.repo &&\
	cd /root/ &&\
	mkdir -p tmp &&\
	cd tmp &&\
	yumdownloader --source php
RUN \
	cd /root/tmp/ &&\
	rpm -ivh php-* &&\
	tar xfj /root/rpmbuild/SOURCES/php-5*.tar.bz2 &&\
	cd php*/ext/sqlite/ &&\
	phpize &&\
	./configure &&\
	make &&\
	make install &&\
	cd /root/ &&\
	rm -fr tmp &&\
	echo 'extension=sqlite.so' >/etc/php.d/sqlite2.ini

EXPOSE 80 443
CMD php -i |grep SQLite
