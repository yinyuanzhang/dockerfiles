FROM ennexa/centos

RUN yum update -y && \
    yum install -y gcc gcc-c++ make redhat-rpm-config libxml2-devel pkgconfig \
    openssl-devel bzip2-devel curl-devel libpng-devel libjpeg-devel libXpm-devel \
    freetype-devel gmp-devel libmcrypt-devel mariadb-devel aspell-devel recode-devel \
    autoconf bison re2c libicu-devel systemd-devel systemtap-sdt-devel \
    ruby-devel rubygems libffi libffi-devel gnupg2 @"Development Tools" rsync \
    && yum clean -y all \
    && rm -rf /var/cache/yum
