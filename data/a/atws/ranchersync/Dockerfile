FROM hermsi/alpine-sshd

RUN apk add --update sudo shadow openssl bash rsync curl php-cli nano php-curl php-json sshpass && \
    rm -rf /tmp/* /var/cache/apk/* && \
    mkdir /sync && \
    sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config && \
    sed -i s/#\ %wheel\ ALL=\(ALL\)\ NOPASSWD:\ ALL/%wheel\ ALL=\(ALL\)\ NOPASSWD:\ ALL/ /etc/sudoers

ADD sync.php /sync/
ADD docker-entrypoint.sh /

RUN chmod +x /docker-entrypoint.sh && \
    mkdir /var/mail && \
    useradd -ms /bin/bash ranchersync && \
    usermod -a -G wheel ranchersync && \
    usermod -a -G adm ranchersync

EXPOSE 22

ENTRYPOINT ["/docker-entrypoint.sh"]
