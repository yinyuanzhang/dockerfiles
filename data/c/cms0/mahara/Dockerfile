FROM php:7.2-apache-stretch
LABEL maintainer="Christian-Maximilian Steier"

ARG VERSION=19.04
ARG RELEASE=.1
ARG minimal_apt_get_install='apt-get install -y --no-install-recommends'
ENV DEBIAN_FRONTEND=noninteractive \
DEBCONF_NONINTERACTIVE_SEEN=true

# copy local files
COPY build/root/ /
# Scripts
ADD build/scripts /scripts
RUN \
    # Cleanup Based on https://gist.github.com/jumanjiman/f9d3db977846c163df12 \
    export sysdirs="/bin /etc /lib /sbin /usr" && \
    echo "[i] Remove crufty...\n   /etc/shadow-\n   /etc/passwd-\n   /etc/group-" && \
    find $sysdirs -xdev -type f -regex '.*-$' -exec rm -f {} + && \
    echo "[i] Ensure system dirs are owned by root and not writable by anybody else." && \
    find $sysdirs -xdev -type d -exec chown root:root {} \; -exec chmod 0755 {} \; && \
    echo "[i] Set wright permissions for /tmp and /var/tmp." && \
    chmod a=rwx,o+t /tmp /var/tmp && \
    echo "[i] Remove unnecessary user accounts." && \
    for user in $(cat /etc/passwd | awk -F':' '{print $1}' | grep -ve root -ve nobody -ve daemon -ve www-data -ve nologin -ve _apt); do deluser "$user"; done && \
    for group in $(cat /etc/group | awk -F':' '{print $1}' | grep -ve root -ve nobody -ve nogroup -ve www-data -ve node -ve staff); do delgroup "$group"; done && \
    echo "[i] Remove interactive login shell" && \
    sed -i -r 's#^(.*):[^:]*$#\1:/sbin/nologin#' /etc/passwd && \
    echo "[i] Remove init scripts" && \
    rm -fr /etc/init.d /lib/rc /etc/conf.d /etc/inittab /etc/runlevels /etc/rc.conf && \
    echo "[i] Remove kernel tunables" && \
    rm -fr /etc/sysctl* /etc/modprobe.d /etc/modules /etc/mdev.conf /etc/acpi && \
    echo "[i] Remove broken symlinks." && \
    find $sysdirs -xdev -type l -exec test ! -e {} \; -delete && \
    \
    /scripts/prepare.sh && \
    \
    # System services \
    echo "\n[i] Install s6-overlay\n" && \
    $minimal_apt_get_install curl gnupg && \
    GPG="DB30 1BA3 F6F8 07E0 D0E6  CCB8 6101 B278 3B2F D161" && \
    S6OVERLAY=$(curl -s https://api.github.com/repos/just-containers/s6-overlay/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")') && \
    if [ $(uname -m) = "armv6l" ] || [ $(uname -m) = "armv7l" ]; then ARCHTAG=armhf ; elif [ $(uname -m) = "aarch64" ]; then ARCHTAG=aarch64 ; elif [ $(uname -m) = "x86_64" ]; then ARCHTAG=amd64 ; fi && \
    curl -o /tmp/s6-overlay.tar.gz -L https://github.com/just-containers/s6-overlay/releases/download/${S6OVERLAY}/s6-overlay-${ARCHTAG}.tar.gz && \
    curl -o /tmp/s6-overlay.tar.gz.sig -L https://github.com/just-containers/s6-overlay/releases/download/${S6OVERLAY}/s6-overlay-${ARCHTAG}.tar.gz.sig && \
    curl https://keybase.io/justcontainers/key.asc | gpg --import && \
    FINGERPRINT="$(LANG=C gpg --verify /tmp/s6-overlay.tar.gz.sig /tmp/s6-overlay.tar.gz 2>&1 | sed -n "s#Primary key fingerprint: \(.*\)#\1#p")" && \
    gpg --verify /tmp/s6-overlay.tar.gz.sig /tmp/s6-overlay.tar.gz && \
    if [ -z "${FINGERPRINT}" ]; then echo "[!!] Invalid GPG signature!" && exit 1; fi && \
    if [ "${FINGERPRINT}" != "${GPG}" ]; then echo "[!!] Wrong GPG fingerprint!" && exit 1; fi && \
    echo "[i] All seems good, now unpacking s6-overlay.tar.gz" && \
    tar xzf /tmp/s6-overlay.tar.gz -C / && \
    \
    echo "\n[i] Install cron\n" && \
    $minimal_apt_get_install cron && \
    \
    # PHP \
    /scripts/php-extensions.sh && \
    \
    # Composer \
    echo "\n[i] Install Composer\n" && \
    curl -sS https://getcomposer.org/installer | php && \
    chmod +x ./composer.phar && \
    mv ./composer.phar /usr/local/bin/composer && \
    \
    # Mahara
    echo "\n[i] Install Mahara\n" && \
    curl -LO https://launchpad.net/mahara/${VERSION}/${VERSION}${RELEASE}/+download/mahara-${VERSION}${RELEASE}.tar.gz && \
    curl -o mahara-${VERSION}${RELEASE}.tar.gz.md5 -L https://launchpad.net/mahara/${VERSION}/${VERSION}${RELEASE}/+download/mahara-${VERSION}${RELEASE}.tar.gz/+md5 && \
    echo "[i] Verifying integrity..." && \
    CHECKSUM_STATE=$(echo -n $(md5sum -c mahara-${VERSION}${RELEASE}.tar.gz.md5) | tail -c 2) && \
    if [ "${CHECKSUM_STATE}" != "OK" ]; then echo "[!!] Checksum does not match!" && exit 1; fi && \
    echo "[i] All seems good, now unpacking mahara-${VERSION}${RELEASE}.tar.gz" && \
    mkdir -p /usr/src/mahara && \
    tar --strip-components=2 -xf mahara-${VERSION}${RELEASE}.tar.gz -C /usr/src/mahara --verbose && \
    rm mahara-${VERSION}${RELEASE}.* && \
    a2enmod rewrite headers expires && \
    \
    # Cleanup \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false git-core && \
    apt-get clean && \
    rm -rf \
        /etc/machine-id \
        /var/lib/dbus/machine-id \
        /var/lib/apt/lists/* \
        /var/log/alternatives.log \
        /var/log/apt/history.log \
        /var/log/apt/term.log \
        /var/log/dpkg.log \
        /etc/ssh/ssh_host_* \
        /var/cache/ldconfig/aux-cache \
        /usr/share/doc \
        /usr/share/man/ \
        /usr/share/info/* \
        /var/cache/man/*  \
        /tmp/* \
        /etc/fstab \
        /scripts \
        /etc/services.d/php-fpm

ENTRYPOINT ["/init"]
