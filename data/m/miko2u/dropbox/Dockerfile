FROM miko2u/centos6
MAINTAINER miko@cafelounge.net

# packages
RUN yum -y update && yum -y install tar && yum clean all \
 && cd /tmp \
 && curl -OL http://www.dropbox.com/download?dl=packages/dropbox.py \
 && chmod a+x dropbox.py \
 && mv dropbox.py /usr/bin/dropbox \
 && useradd -m dropbox \
 && cd /home/dropbox \
 && curl -L https://www.dropbox.com/download?plat=lnx.x86_64 -o dropbox.tar.gz \
 && tar zxvf dropbox.tar.gz \
 && chown -R dropbox:dropbox .dropbox-dist \
 && rm dropbox.tar.gz

# ADD dropbox.init /etc/init.d/dropbox
#RUN chmod a+x /etc/init.d/dropbox
# && chkconfig --add dropbox \
# && chkconfig dropbox on

# change init
ADD boot/* /boot/
