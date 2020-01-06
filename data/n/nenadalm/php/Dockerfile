FROM nenadalm/fedora

RUN yum install -y \
    git \
    make \
    wget \
    gcc \
    mod_fcgid \
    tar \
    bzip2 \
    autoconf \
    libxml2-devel \
    libcurl-devel \
    postgresql-devel \
    openssl-devel \
    libssh2-devel \
    openldap-devel \
    turbojpeg-devel \
    libjpeg-turbo-devel \
    libpng-devel \
    libicu-devel \
    libmcrypt-devel \
    ImageMagick-devel \
    librabbitmq-devel \
    gcc-c++

RUN git clone https://github.com/fpoirotte/phpfarm.git /opt/phpfarm
COPY configuration /

ENV PATH $PATH:/opt/phpfarm/inst/current/bin
RUN /opt/phpfarm/src/main.sh 5.6.4-pear
RUN /opt/phpfarm/inst/bin/switch-phpfarm 5.6.4

ENV TERM xterm

