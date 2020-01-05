FROM centos:7

RUN set -x \
    && echo start \
    && rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 \
    \
    && yum -y install epel-release \
    && rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 \
    \
    && yum -y install tigervnc-server \
    && yum -y groupinstall Xfce \
    \
    && useradd user \
    && echo "user:user" | chpasswd \
    \
    && yum clean all \
    \
    && echo done

USER user

RUN mkdir ~/.vnc \
    && (echo user | vncpasswd -f > ~/.vnc/passwd) \
    && chown -R user:user ~/.vnc \
    && chmod 0600 ~/.vnc/passwd \
    && echo -e "\ 
unset SESSION_MANAGER\n \
unset DBUS_SESSION_BUS_ADDRESS\n \
exec xfce4-session &\n" \ 
> ~/.vnc/xstartup \
    && chmod +x ~/.vnc/xstartup

CMD ["sh", "-c", "vncserver; tail -f /dev/null"]
