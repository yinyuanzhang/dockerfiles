FROM nfnty/arch-mini:latest

MAINTAINER "Ian Reinhart Geiser <geiseri@yahoo.com>"
ENV container docker

#install our stuff over base image
RUN echo "[repo]" >> /etc/pacman.conf && \
    echo "SigLevel = Optional TrustAll" >> /etc/pacman.conf && \
    echo "Server = http://geiseri.com/packages/repo" >> /etc/pacman.conf && \
    pacman -Suy --noconfirm && \
    pacman -S --noconfirm --needed \
                                   base base-devel devtools sudo git \
                                   qt5 qt5-doc qtcreator \
                                   gdb cmake valgrind clang \
                                   xorg-xauth x11-ssh-askpass \
                                   xorg-server pulseaudio openssh \
                                   pwgen ttf-bitstream-vera \
                                   ttf-inconsolata systemd \
                                   python2-virtualenv python-virtualenv \
                                   sudo xfce4-terminal openbox \
                                   firefox flashplugin thunar thunar-archive-plugin \
                                   geany geany-plugins zip unzip \
                                   elfutils bash-completion \
                                   cloud-init hicolor-icon-theme \
                                   qtcurve-gtk2 qtcurve-qt5 qtcurve-qt4 qtcurve-utils \
                                   elementary-icon-theme \
                                   polkit-qt5 poppler-qt5 \
                                   attica-qt5 \
                                   qwt5 pam_mount \
                                   xrdp x11rdp tint2-git obmenu-generator \
                                   quazip-qt5  qxmpp-qt5 cutemarked qmlsystray-git \
                                   uncrustify qt5ct xcbsupport qtsystemd qtftp-qt5 \
                                   grantlee-qt5 qamqp-git qml-material smtpclient-qt5-git \
                                   && \
    pacman -Scc --noconfirm


# Set locale (fix the locale warnings)
RUN localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 || :

# configure X
RUN echo "allowed_users = anybody" > /etc/X11/Xwrapper.config && \
    echo "needs_root_rights = no" >> /etc/X11/Xwrapper.config
	
ADD systemd/systemd-tmpfiles-setup.service /etc/systemd/system/systemd-tmpfiles-setup.service.d/ignoresysfs.conf
ADD systemd/limits.conf /etc/security/limits.conf

# configure desktop
ADD support/openbox.rc.xml /etc/xdg/openbox/rc.xml
ADD support/openbox.menu.xml /etc/xdg/openbox/menu.xml
ADD support/obmenu-schema.pl /etc/xdg/obmenu-generator/schema.pl
ADD support/tint2rc /etc/xdg/tint2/tint2rc
ADD support/cloud.cfg /etc/cloud/cloud.cfg
ADD support/rdp-login.pam /etc/pam.d/xrdp-sesman
ADD support/xrdp-startwm.sh /etc/xrdp/startwm.sh
ADD support/xrdp.ini /etc/xrdp/xrdp.ini 

RUN ln -s /etc/fonts/conf.avail/75-ttf-inconsolata.conf /etc/fonts/conf.d/75-ttf-inconsolata.conf && \
    chmod +x  /etc/xrdp/startwm.sh

# Configure up systemd
RUN \
    systemctl enable xrdp.service && \
    systemctl enable cloud-init.service && \
    systemctl enable cloud-config.service && \
    systemctl enable cloud-final.service && \
    systemctl set-default multi-user.target && \
    useradd --system -U syslog

# Setup cloud-init
RUN mkdir -p /var/lib/cloud/seed/nocloud-net && \
    touch /var/lib/cloud/seed/nocloud-net/meta-data && \
    mkdir -p /var/lib/cloud/seed/nocloud

# Expose resources
VOLUME ["/sys/fs/cgroup","/var/lib/cloud/seed/nocloud"]
EXPOSE  3389  22

CMD ["lib/systemd/systemd"]
