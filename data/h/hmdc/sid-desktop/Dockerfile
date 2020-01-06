FROM hmdc/xpra:1.2.0-2
EXPOSE 8080
RUN useradd -G xpra -m -s /bin/bash sid-user && \
    yum -y update
COPY start-lxqt.sh /usr/bin
COPY scripts/install-applications.sh /usr/bin
RUN yum -y install git
RUN bash /usr/bin/install-applications.sh && \  
    chmod a+x /usr/bin/start-lxqt.sh && \
    mkdir -p /run/xpra && \
    chmod 777 /run/xpra && \
    mkdir -p /run/user/1000/xpra && \
    chown -R sid-user:xpra /run/user/1000/xpra && \
    mkdir /tmp/.X11-unix && \
    chmod 1777 /tmp/.X11-unix && \
    chown root /tmp/.X11-unix/ && \
    rm -f /etc/xdg/autostart/lxpolkit.desktop /etc/xdg/autostart/clipit-startup.desktop /etc/xdg/autostart/lxqt-xscreensaver-autostart.desktop /etc/xdg/autostart/nm-tray-autostart.desktop && \
    dbus-uuidgen > /var/lib/dbus/machine-id && \
    strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5
COPY config/etc-xdg-lxqt/* /etc/xdg/lxqt/
RUN cp -R /usr/share/themes/Clearlooks-3.4 /usr/share/themes/Sid && \
    sed -i -e '/<theme>/{N;s/<name>.*<\/name>/<name>Sid<\/name>/;}' /etc/xdg/openbox/lxqt-rc.xml
COPY config/etc/sudoers /etc/sudoers
RUN dnf -y --setopt=tsflags= install man-db man-pages
# Remove the Xpra desktop background per https://github.com/hmdc/sid/issues/617#issuecomment-539994925
RUN rm -f /usr/share/xpra/www/background.png

USER sid-user
# Install Ista's emacs configuration to home directory
#  preceded by installing the current ELPA GPG key per http://elpa.gnu.org/packages/gnu-elpa-keyring-update.html
RUN git clone https://github.com/IQSS/IQSS.emacs.git ~/.emacs.d && \
    mkdir -p ~/.emacs.d/elpa/gnupg && gpg --homedir ~/.emacs.d/elpa/gnupg --receive-keys 066DAFCB81E42C40 && \
    env EMACS_AUTOINSTALL_PACKAGES=yes emacs -batch --script ~/.emacs.d/init.el

ENTRYPOINT ["/usr/bin/start-lxqt.sh"]
