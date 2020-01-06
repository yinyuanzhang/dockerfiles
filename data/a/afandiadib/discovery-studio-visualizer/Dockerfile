FROM centos:7

MAINTAINER "Adib Afandi bin Abdullah <fendy90.oscura@gmail.com>"

RUN yum -y update && \
    yum -y install alsa-lib.i686 audit-libs.x86_64 audit-libs.i686 compat-libstdc++-33.i686 e2fsprogs-libs.x86_64 e2fsprogs-libs.i686 expat.i686 expat.x86_64 glibc.i686 keyutils-libs.i686 krb5-libs.i686 libgcc.i686 libICE.i686 libpcap.i686 libselinux.i686 libsepol.i686 libSM.i686 libstdc++.i686 libX11.i686 libXau.i686 libXdmcp.i686 libXext.i686 libXi.i686 libXmu.i686 libXp.i686 libXp.x86_64 libXpm.i686 libXpm.x86_64 libXrender.i686 libXt.i686 libXtst.i686 pam.i686 cairo.i686 cairo.x86_64 fontconfig.x86_64 fontconfig.i686 glib2.i686 glib2.x86_64 bzip2-libs.x86_64 bzip2-libs.i686 freetype.x86_64 freetype.i686 libjpeg-turbo.i686 libjpeg-turbo.x86_64 libtiff.i686 libtiff.x86_64 zlib.i686 libdrm.i686 libdrm.x86_64 libXdamage.i686 libXfixes.i686 libXxf86vm.i686 libXinerama.i686 tcsh bc compat-libstdc++-296.i686 compat-libtermcap.i686 cracklib.i686 cyrus-sasl-lib.x86_64 gamin.i686 libdbi.i686 libuuid.i686 libxcb.i686 libXcursor.i686 libXrandr.i686 mesa-dri-drivers.i686 mesa-libGL.i686 mesa-libGLU.i686 mesa-libGLU.x86_64 ncurses-libs.x86_64 ncurses-libs.i686 nspr.i686 pixman.x86_64 libcom_err.i686 glib2-devel.i686 glib2-devel.x86_64 pcre.i686 pcre.x86_64 compat-db47.i686 && \
    yum -y install gstreamer-plugins-base.x86_64 xorg-x11-drv-ati xorg-x11-drv-dummy xorg-x11-drv-evdev xorg-x11-drv-fbdev xorg-x11-drv-intel xorg-x11-drv-nouveau xorg-x11-drv-qxl xorg-x11-drv-synaptics xorg-x11-drv-v4l xorg-x11-drv-vesa xorg-x11-drv-vmmouse xorg-x11-drv-vmware xorg-x11-drv-void xorg-x11-drv-wacom xorg-x11-font-utils xorg-x11-fonts-Type1 xorg-x11-proto-devel xorg-x11-server-common xorg-x11-server-utils xorg-x11-xkb-utils mesa-filesystem mesa-libEGL mesa-libGL mesa-libGLES mesa-libgbm mesa-libwayland-egl mesa-libxatracker libX11-devel libXau-devel libXcomposite libXcursor libXdamage libXdmcp libXfixes libXfont libXfont2 libXft libXi libXinerama libXrandr libXrender libXres libXtst libXv libXvMC libXxf86dga libXxf86misc libXxf86vm mesa-dri-drivers xorg-x11-drivers xorg-x11-utils xorg-x11-xinit xorg-x11-server-Xorg && \
    yum -y install unzip wget perl && \
    wget https://github.com/ericchiang/pup/releases/download/v0.4.0/pup_v0.4.0_linux_amd64.zip && \
    unzip pup_v0.4.0_linux_amd64.zip && chmod +x pup && \
    filename=dsv2017R2.tar.gz && \
    fileid=1o5KZmQ-JxK-ntPCqQENRoAsayrCqOd3M && \
    query=`curl -c ./cookie.txt -s -L "https://drive.google.com/uc?export=download&id=${fileid}" | ./pup 'a#uc-download-link attr{href}' | sed -e 's/amp;//g'` && \
    curl -s -b ./cookie.txt -L -o ${filename} "https://drive.google.com${query}" && \
    tar -xf dsv2017R2.tar.gz -C /opt/ && \
    rm dsv2017R2.tar.gz pup && \
    yum -y remove unzip wget && yum -y clean all && rm -rf /var/cache/yum

ENV QT_GRAPHICSSYSTEM="native"

CMD /opt/BIOVIA/DiscoveryStudio2017R2/bin/DiscoveryStudio2017R2
