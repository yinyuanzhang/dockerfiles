FROM abuisine/nvidia:375.66-7

LABEL maintainer="Alexandre Buisine <alexandrejabuisine@gmail.com>" version="${NVIDIA_DRIVER_VERSION}-13"

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update \
 && apt-get install --no-install-recommends -yqq \
 	x11-apps \
 	xserver-xorg-video-dummy \
	libgtk-3-0 \
	libxv1 \
	vim-tiny \
 && apt-get -yqq clean \
 && rm -rf /var/lib/apt/lists/*

COPY resources/nvidia_drv.so /usr/lib/xorg/modules/drivers/ 
COPY resources/nvidia-drm-outputclass.conf /usr/share/X11/xorg.conf.d/ 
COPY resources/nvidia-settings /usr/bin/nvidia-settings 
COPY resources/libnvidia-gtk3.so.${NVIDIA_DRIVER_VERSION} /usr/lib/x86_64-linux-gnu/libnvidia-gtk3.so.${NVIDIA_DRIVER_VERSION} 
COPY resources/docker-entrypoint.py resources/Xorg.py resources/NvidiaSettings.py /usr/local/bin/

RUN chmod +x /usr/bin/nvidia-settings /usr/local/bin/docker-entrypoint.py

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.py"]