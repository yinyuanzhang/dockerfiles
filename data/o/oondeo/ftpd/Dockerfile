FROM debian:stretch

ENV SUMMARY="SSHD and FTP Image"	\
    DESCRIPTION="SSHD and FTP Image, also have rsync and git commands to use with ssh. The image use scripts and configurations compatible \
        with redhat openshift."

LABEL summary="$SUMMARY" \
      description="$DESCRIPTION" \
      io.k8s.description="$DESCRIPTION" \
      io.k8s.display-name="vsftpd" \
      io.openshift.s2i.scripts-url=image:///usr/libexec/s2i/bin \
      io.s2i.scripts-url=image:///usr/libexec/s2i/bin \
      com.redhat.component="core" \
      name="oondeo/vsftpd" \
      version="3.0.3" \
      release="2" \
maintainer="OONDEO <info@oondeo.es>"

ENV \
    # DEPRECATED: Use above LABEL instead, because this will be removed in future versions.
    STI_SCRIPTS_URL=image:///usr/libexec/s2i \
    # Path to be used in other layers to place s2i scripts into
    STI_SCRIPTS_PATH=/usr/libexec/s2i/bin

ENV \
    # The $HOME is not set by default, but some applications needs this variable
    HOME=/opt/app-root/src \
    PATH=/opt/app-root/src/bin:/opt/app-root/bin:$STI_SCRIPTS_PATH:$PATH 
    

ENV CHROOT="no" PASSIVE_PORTS="60000:60010" SSH_PORT="10022" FTP_PORT="10021" FTPD_PORT="10020" ADDRESS="" 

COPY root/root/ /

RUN docker-header

RUN apt-get update && apt-get install -y --no-install-recommends openssh-server proftpd inotify-tools \
    && mkdir -p /opt/app-root/etc/ssh \
    && mv /var/log/proftpd /opt/app-root/var/log && ln -s /opt/app-root/var/log /var/log/proftpd \
    && rm -rf /tmp/* /var/tmp/* /var/lib/apt/* /var/cache/*

EXPOSE 10020 10021 10022 60000-65535

ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/sbin/tini", "-g" ,"--", "/usr/bin/container-entrypoint"]

# COPY etc/vsftpd.virtual /etc/pam.d/
COPY etc/ /etc/
COPY s2i/bin $STI_SCRIPTS_PATH

# VOLUME /opt/app-root/etc

RUN docker-footer \ 
    && sed -i 's/1001\:\!/1001:*/g' /etc/shadow \
    && chown -R root:root /opt/app-root \
    && chown root:root /etc/shadow && chmod 660 /etc/shadow \
    && chmod 660 /var/log \
    && chmod go-w /opt/app-root/etc /opt/app-root /opt 



USER 1001

ENTRYPOINT [ "container-entrypoint" ]
CMD [ "$STI_SCRIPTS_PATH/run" ]

