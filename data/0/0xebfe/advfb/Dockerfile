FROM binhex/arch-delugevpn:latest
RUN pacman -S --needed p7zip --noconfirm
RUN pacman -S --needed speedtest-cli --noconfirm
RUN pacman -S --needed jre8-openjdk --noconfirm
RUN pacman -S --needed wget --noconfirm
RUN pacman -S --needed unzip --noconfirm
RUN pacman -S --needed ca-certificates --noconfirm
ARG FB_VER=4.7.9
RUN mkdir -p /opt/filebot \
    && cd /opt/filebot \
    && wget -O FileBot_${FB_VER}-portable.tar.xz https://sourceforge.net/projects/filebot/files/filebot/FileBot_${FB_VER}/FileBot_${FB_VER}-portable.tar.xz/download \
    && tar -xvf FileBot_${FB_VER}-portable.tar.xz \
    && chmod -R 777 /opt/filebot \
    && rm -f /opt/filebot/FileBot_${FB_VER}-portable.tar.xz \
    && sed -i -e"s/useExtendedFileAttributes=true/useExtendedFileAttributes=false/" /opt/filebot/filebot.sh

