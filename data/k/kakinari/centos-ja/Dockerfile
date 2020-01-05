FROM centos:7
ENV container docker
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
systemd-tmpfiles-setup.service ] || rm -f $i; done; cd /;\
sed -i '/^override_install_langs=/d' /etc/yum.conf;\
sed -i 's/.*/LANG=ja_JP.UTF-8\nLANGUAGE=ja_JP:ja/' /etc/locale.conf;\
yum -y --nogpgcheck reinstall glibc-common;\
yum -y upgrade; yum -y clean all); \
rm -rf /var/cache/yum/*;\
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;\
cp -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
VOLUME /sys/fs/cgroup
CMD /usr/sbin/init
