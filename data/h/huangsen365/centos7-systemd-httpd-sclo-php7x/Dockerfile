FROM centos/systemd

MAINTAINER "Your Name" <you@example.com>

RUN sed -i 's/tsflags=nodocs/\#tsflags=nodocs/g' /etc/yum.conf
RUN echo "ip_resolve=4" >> /etc/yum.conf
RUN yum -y update
RUN yum -y install man-pages man-db man

RUN echo "export HISTSIZE=999999999" >> /etc/bashrc
RUN echo "export HISTTIMEFORMAT=\"%F %T \"" >> /etc/bashrc
RUN echo "export VISUAL=\"vim\"" >> /etc/bashrc
RUN echo "export EDITOR=\"vim\"" >> /etc/bashrc

RUN rm -rf /etc/localtime
RUN ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN yum makecache fast
RUN yum -y --enablerepo=extras install epel-release centos-release-scl
RUN yum -y install scl-utils
RUN yum -y install bzip2 \
cronie \
git \
htop \
httpd \
iftop \
logrotate \
mariadb-server \
mod_ssl \
mtr \
mysql \
nginx \
openssh-clients \
openssh-server \
php \
php-fpm \
php-gd \
php-imap \
php-mbstring \
php-mcrypt \
php-mysql \
php-odbc \
php-pear \
php-pecl-geoip \
php-pecl-memcached \
php-pecl-redis \
php-pgsql \
php-snmp \
php-xml \
php-xmlrpc \
redis \
rsync \
subversion \
sudo \
telnet \
tmux \
unar \
unzip \
vim-enhanced \
wget \
zip \
zlib-devel

COPY vimrc_append_conf.txt /tmp
RUN cat /tmp/vimrc_append_conf.txt >> /etc/vimrc

RUN yum -y install rh-php70 rh-php70-php rh-php70-php-fpm rh-php70-php* sclo-php70-php* --exclude=sclo-php70-php-pecl-redis --exclude=sclo-php70-php-smbclient --exclude=sclo-php70-php-pecl-redis4*
RUN yum -y install rh-php71 rh-php71-php rh-php71-php-fpm rh-php71-php* sclo-php71-php* --exclude=sclo-php71-php-pecl-redis --exclude=sclo-php71-php-smbclient --exclude=sclo-php71-php-pecl-redis4*
#RUN yum -y install rh-php72 rh-php72-php rh-php72-php-fpm rh-php72-php* sclo-php72-php* --exclude=sclo-php72-php-pecl-redis --exclude=sclo-php72-php-smbclient --exclude=sclo-php72-php-pecl-redis4*

RUN useradd sshuser
RUN usermod -aG apache sshuser
#RUN mv /etc/opt/rh/rh-php71/php-fpm.d/www.conf /etc/opt/rh/rh-php71/php-fpm.d/www.conf.bak
COPY php-fpm_9001_www.yourdomain.com.conf /etc/opt/rh/rh-php71/php-fpm.d/php-fpm_9001_www.yourdomain.com.conf.bak
COPY php-fpm_9001_www.yourdomain.com.conf /etc/opt/rh/rh-php71/php-fpm.d/php-fpm_9001_www.yourdomain.com.conf
COPY httpd_9001_www.yourdomain.com.conf /etc/httpd/conf.d/httpd_9001_www.yourdomain.com.conf.bak
COPY httpd_9001_www.yourdomain.com.conf /etc/httpd/conf.d/httpd_9001_www.yourdomain.com.conf

COPY httpd.conf /etc/httpd/conf/httpd.conf
COPY mkdir.sh /tmp/mkdir.sh
COPY rsync.sh /tmp/rsync.sh
COPY mkdir_chown_chmod.sh /root/mkdir_chown_chmod.sh


RUN sh /tmp/mkdir.sh
RUN sh /tmp/rsync.sh
RUN systemctl enable httpd.service; systemctl enable rh-php71-php-fpm; systemctl enable sshd

#RUN yum clean all

#RUN /bin/sh /root/mkdir_chown_chmod.sh
RUN rpm -v --import https://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
RUN rpm -Uvh https://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
RUN yum install -y ffmpeg ffmpeg-devel

EXPOSE 80 443

CMD ["/usr/sbin/init"]
