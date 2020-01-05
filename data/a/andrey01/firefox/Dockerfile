FROM ubuntu:zesty
MAINTAINER Andrey Arapov <andrey.arapov@nixaid.com>

# To avoid problems with Dialog and curses wizards
ENV DEBIAN_FRONTEND noninteractive

# Keep the image updated and install the dependencies
RUN apt-get update && \
    apt-get -y --no-install-recommends install ca-certificates tzdata \
                       bzip2 libgtk2.0-0 libgtk-3-0 libdbus-glib-1-2 libxt6 attr \
                       pulseaudio libgl1-mesa-glx x264 \
                       libpango1.0-0 libv4l-0 \
                       fonts-dejavu-core fonts-freefont-ttf fonts-guru-extra \
                       fonts-kacst fonts-kacst-one fonts-khmeros-core fonts-lao \
                       fonts-liberation fonts-lklug-sinhala fonts-lohit-guru \
                       fonts-nanum fonts-opensymbol fonts-sil-abyssinica \
                       fonts-sil-padauk fonts-symbola fonts-takao-pgothic \
                       fonts-tibetan-machine fonts-tlwg-garuda-ttf \
                       fonts-tlwg-kinnari-ttf fonts-tlwg-laksaman-ttf \
                       fonts-tlwg-loma-ttf fonts-tlwg-mono-ttf \
                       fonts-tlwg-norasi-ttf fonts-tlwg-purisa-ttf \
                       fonts-tlwg-sawasdee-ttf fonts-tlwg-typewriter-ttf \
                       fonts-tlwg-typist-ttf fonts-tlwg-typo-ttf \
                       fonts-tlwg-umpush-ttf fonts-tlwg-waree-ttf \
                       ttf-bitstream-vera ttf-dejavu-core ttf-ubuntu-font-family \
                       fonts-arphic-ukai fonts-arphic-uming \
                       fonts-ipafont-mincho fonts-ipafont-gothic \
                       fonts-unfonts-core && \
    rm -rf /var/lib/apt/lists

# Workaround: pulseaudio client library likes to remove /dev/shm/pulse-shm-*
#             files created by the host, causing sound to stop working.
#             To fix this, we either want to disable the shm or mount /dev/shm
#             in read-only mode when starting the container.
RUN echo "enable-shm = no" >> /etc/pulse/client.conf

# Mozilla Firefox
# Deps: bzip2 libgtk-3-0 libdbus-glib-1-2 libxt6
ENV FIREFOX_VER 56.0
ADD https://download-installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VER/linux-x86_64/en-US/firefox-$FIREFOX_VER.tar.bz2 /tmp/firefox.tar.bz2
RUN cd /tmp && \
    mkdir /opt/mozilla && \
    tar xf firefox.tar.bz2 -C /opt/mozilla/ && \
    rm -f firefox.tar.bz2 && \
    chown -Rh root:root /opt/mozilla

# Define a user under which the Firefox will be running
ENV USER user
ENV UID 1000
ENV GROUPS video,audio
ENV HOME /home/$USER
RUN useradd -u $UID -m -d $HOME -s /usr/sbin/nologin -G $GROUPS $USER

WORKDIR $HOME

# Java JRE requires /tmp directory to be writable
VOLUME [ "/tmp" ]

COPY ./launch /launch
ENTRYPOINT [ "/bin/bash", "/launch" ]
