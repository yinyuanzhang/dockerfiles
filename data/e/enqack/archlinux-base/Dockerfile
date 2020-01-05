#enqack/archlinux-base

###########################################################
# Dockerfile for another custom Arch Linux base container
############################################################

FROM dock0/arch
MAINTAINER enqack <enqack@gmail.com>

ENV TERM xterm
WORKDIR /tmp

RUN pacman -Syyu --noconfirm && \

    ## Configure pacman

    # Fix for failed: IPC connect call failed
    dirmngr </dev/null > /dev/null 2>&1 && \

    # Allow for colored output in pacman.conf
    sed -i "s/#Color/Color/" /etc/pacman.conf && \

    # Archlinux CN repo (has yaourt and sometimes other interesting tools)
    echo "[archlinuxcn]" >> /etc/pacman.conf && \
    echo "SigLevel = Optional TrustAll" >> /etc/pacman.conf && \
    echo "Server = http://repo.archlinuxcn.org/\$arch" >> /etc/pacman.conf && \

    # Add multilib repo
    sed -i '/#\[multilib\]/,/#Include = \/etc\/pacman.d\/mirrorlist/ s/#//' /etc/pacman.conf && \
    sed -i '/#\[multilib\]/,/#Include = \/etc\/pacman.d\/mirrorlist/ s/#//' /etc/pacman.conf && \
    sed -i 's/#\[multilib\]/\[multilib\]/g' /etc/pacman.conf && \

    # Update and force a refresh of all package lists even if they appear up to date.
    pacman -Syyu --noconfirm && \

    # Install all the repo keyrings and mirrorlists
    pacman --noconfirm -S \
    archlinuxcn-keyring && \

    # Install yaourt, package-query and cower for easy AUR usage.
    # TODO make sure package query still exists later after yaourt uninstall
    pacman -S --noconfirm yaourt package-query cower

# TODO switch to rankmirrors since its built in for pacman.
# Setup pacman to use the fastest mirrors.
RUN pacman -S reflector --noconfirm && \
    reflector --verbose -l 5 --protocol https --sort rate --save /etc/pacman.d/mirrorlist && \
    pacman -Rs reflector --noconfirm

# Reinstall openssl without a Perl dependency (This really isn't needed. Seriously)
    # Patch makepkg so we can run as it as root.
RUN sed -i 's/EUID == 0/EUID == -1/' /usr/bin/makepkg && \
    pacman --noconfirm -S wget file patch binutils gcc autoconf make fakeroot && \
    wget --content-disposition "https://projects.archlinux.org/svntogit/packages.git/plain/trunk/ca-dir.patch?h=packages/openssl" && \
    wget --content-disposition "https://projects.archlinux.org/svntogit/packages.git/plain/trunk/no-rpath.patch?h=packages/openssl" && \
    wget --content-disposition "https://projects.archlinux.org/svntogit/packages.git/plain/trunk/PKGBUILD?h=packages/openssl" && \
    sed -i "s/depends=('zlib' 'perl')/depends=('zlib')/" PKGBUILD && \
    sed -i "s/make test//" PKGBUILD && \
    makepkg --noconfirm -si --skippgpcheck && \

    # Unpatch makepkg
    sed -i 's/EUID == -1/EUID == 0/' /usr/bin/makepkg

# Create new account that isn't root. user: docker password: docker
RUN useradd --create-home docker && \
    echo -e "docker\ndocker" | passwd docker && \

    # Allow passwordedless sudo for now but we will remove it later.
    pacman --noconfirm -S sudo && \
    echo "docker ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \

    # Replace texinfo with a fake textinfo so we can remove Perl
    runuser -l docker -c "yaourt --noconfirm -Rdd texinfo" && \
    runuser -l docker -c "yaourt --noconfirm -S texinfo-fake" && \

    # Install localepurge
    runuser -l docker -c "yaourt --noconfirm -S localepurge" && \

    # Configure localepurge
    sed -i "s/NEEDSCONFIGFIRST/#NEEDSCONFIGFIRST/" /etc/locale.nopurge && \
    sed -i "s/#DONTBOTHERNEWLOCALE/DONTBOTHERNEWLOCALE/" /etc/locale.nopurge

# Remove stuff we used for compiling packages since huge (219 mB)
RUN pacman --noconfirm -Rs  \
    binutils  \
    gcc \
    make \
    autoconf \
    file \
    patch \

    fakeroot \
    perl \

    # Remove package manager stuff
    yaourt \
    diffutils \
    gettext \

    # Remove other stuff
    util-linux \
    shadow \
    sudo \

    sysfsutils \
    git \

    # (7.1MB) Iproute2 and iptables
    iproute2 \

    # (1.76MB) Utilities for monitoring your system and its processes
    procps-ng \

    # .73 MB
    iputils


# Remove ducktape & shim & leftover mirrorstatus.
RUN rm -r /.ducktape /.shim && \
    rm /tmp/.root.mirrorstatus.json

##########################################################################
# CLEAN UP SECTION - THIS GOES AT THE END                                #
##########################################################################
RUN localepurge && \

    # Remove info, man and docs
    rm -r /usr/share/info/* && \
    rm -r /usr/share/man/* && \
    rm -r /usr/share/doc/* && \

    # was a bit worried about these at first but I haven't seen an issue yet on them.
    rm -r /usr/share/zoneinfo/* && \
    rm -r /usr/share/i18n/* && \

    # Delete any backup files like /etc/pacman.d/gnupg/pubring.gpg~
    find /. -name "*~" -type f -delete && \

    # Keep only xterm related profiles in terminfo.
    find /usr/share/terminfo/. ! -name "*xterm*" ! -name "*screen*" ! -name "*screen*" -type f -delete && \

    # Remove anything left in temp.
    rm -r /tmp/*

RUN bash -c "echo 'y' | pacman -Scc >/dev/null 2>&1" && \
    paccache -rk0 >/dev/null 2>&1 &&  \
    pacman-optimize && \
    rm -r /var/lib/pacman/sync/*

#########################################################################

WORKDIR /
CMD /usr/bin/bash
