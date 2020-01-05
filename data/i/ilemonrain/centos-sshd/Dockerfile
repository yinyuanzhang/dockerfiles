FROM centos:6

LABEL MAINTIANER="iLemonrain <ilemonrain@ilemonrain.com>" \
      ImageVersion="20180920"

COPY source/entrypoint.sh /usr/sbin/init-docker

RUN ( yum makecache && yum update -y ;\
      yum install -y initscripts openssh-server epel-release wget curl \
                     tar unzip zip ;\
      sed -i '/UsePAM yes/s/yes/no/' /etc/ssh/sshd_config; \
      sed -i "/Port/s/#Port/Port/" /etc/ssh/sshd_config ;\
      sed -i "/PermitRootLogin/s/#Permit/Permit/" /etc/ssh/sshd_config ;\
      echo "root:centos" | chpasswd ;\
      cp -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime ;\
      chmod +x /usr/sbin/init-docker ;\
      rm -f /root/anaconda-ks.cfg ;\
      rm -f /root/install* ;\
      yum clean all && rm -rf /var/cache/yum )

EXPOSE 22

WORKDIR /root

ENTRYPOINT [ "/usr/sbin/init-docker" ]