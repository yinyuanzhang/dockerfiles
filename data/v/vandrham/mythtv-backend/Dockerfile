FROM ubuntu:18.04

MAINTAINER Edwin van der Ham <vandrham+docker@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

USER root

ENV LANG en_US	.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get update -y -qq && \
    apt-get install locales software-properties-common -y && \
    locale-gen en_US.UTF-8 && \

# openssh server
    apt-get install -y openssh-server && \

# xnest
    apt-get install -y xnest && \

# supervisor
    apt-get install -y supervisor && \

# pwgen
    apt-get install -y pwgen && \

# mc
    apt-get install -y mc && \

# clean up
    apt-get autoclean && apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* && \

# sshd
    mkdir -p /var/run/sshd && \
    sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && \
    sed -i "s/#PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config && \
    sed -i "s/#PasswordAuthentication/PasswordAuthentication/g" /etc/ssh/sshd_config && \
    sed -i "s/#X11UseLocalhost.*/X11UseLocalhost no/g" /etc/ssh/sshd_config && \

# fix so resolvconf can be configured
    echo "resolvconf resolvconf/linkify-resolvconf boolean false" | debconf-set-selections && \

# create needed folders
    mkdir -p /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix && \
    mkdir -p /var/run/dbus && \

# done
    echo done

COPY ["etc/supervisor/conf.d/*.conf", "/etc/supervisor/conf.d/"]
COPY ["scripts/*.sh", "/"]

EXPOSE 22


ENV USER=mythtv \
    DEBIAN_FRONTEND=noninteractive \
    TERM=xterm

RUN apt-get update -qq && \

# install mythtv-backend, database and ping util
    apt-get install -y --no-install-recommends gettext-base mariadb-server tzdata && \
    sed -i 's/bind-address/#bind-address/' /etc/mysql/mariadb.conf.d/50-server.cnf && \
    apt-get install -y --no-install-recommends mythtv-backend-master mythtv-theme-mythbuntu iputils-ping && \

# mythtv-setup needs xprop
    apt-get install -y x11-utils && \

# create/place required files/folders
    mkdir -p /home/mythtv/.mythtv /var/lib/mythtv /var/log/mythtv /var/run/mysqld /root/.mythtv \
        /mnt/movies /mnt/recordings && \

# set a password for user mythtv and add to required groups
    echo "mythtv:mythtv" | chpasswd && \
    usermod -s /bin/bash -d /home/mythtv -a -G users,mythtv,adm,sudo mythtv && \

# have myth setup use proper start and stop scripts
    sed -i 's#/usr/sbin/service mythtv-backend stop#/usr/bin/supervisorctl stop mythtv#' /usr/bin/mythtv-setup && \
    sed -i 's#/usr/sbin/service mythtv-backend start#/usr/bin/supervisorctl start mythtv#' /usr/bin/mythtv-setup && \

# set permissions for files/folders
    chown -R mythtv:users /var/lib/mythtv /var/log/mythtv /mnt/recordings /mnt/movies && \

# clean up
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
        /usr/share/man /usr/share/groff /usr/share/info \
        /usr/share/lintian /usr/share/linda /var/cache/man && \
    (( find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true )) && \
    (( find /usr/share/doc -empty|xargs rmdir || true ))

# expose ports (UPnP, MythTV backend + API)
EXPOSE 5000/udp 6543 6544 3306
VOLUME /var/lib/mysql/ /mnt/recordings /mnt/movies

RUN ln -s /sbin/initctl /sbin/status

COPY ["etc/mythtv/config.xml", "/etc/mythtv/"]

ENTRYPOINT ["/docker-entrypoint.sh"]