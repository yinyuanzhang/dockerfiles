FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04
MAINTAINER ikeyasu <ikeyasu@gmail.com>

RUN apt-get -y update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
  git \
  libgl1-mesa-dri \
  menu \
  net-tools \
  blackbox \
  python3-pip \
  sudo \
  tint2 \
  x11-xserver-utils \
  x11vnc \
  xinit \
  xserver-xorg-video-dummy \
  xserver-xorg-input-void

RUN apt-get -y clean && \
  rm -rf /var/lib/apt/lists/*

RUN rm -f /usr/share/applications/x11vnc.desktop
RUN pip3 install --upgrade pip
RUN pip3 install websockify supervisor
RUN mkdir -p /var/log/supervisor/

RUN bash -c "ln -s $(which python3) /usr/bin/python && ln -s $(which pip3) /usr/bin/pip"

COPY etc/skel/.xinitrc /etc/skel/.xinitrc

RUN useradd -m -s /bin/bash user
USER user

RUN cp /etc/skel/.xinitrc /home/user/
USER root
RUN echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/user


RUN git clone https://github.com/kanaka/noVNC.git /opt/noVNC && \
  cd /opt/noVNC && \
  git checkout v1.1.0 && \
  ln -s vnc.html index.html

# noVNC (http server) is on 6080, and the VNC server is on 5900
EXPOSE 6080 5900

COPY etc /etc
COPY usr /usr

ENV DISPLAY :0
ENV VNC_PW ""

WORKDIR /root

CMD ["/usr/local/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG IMAGE
ARG VCS_REF
ARG VCS_URL
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name=$IMAGE \
      org.label-schema.description="An image based on Ubuntu 16.04 containing an X_Window_System which supports rendering graphical applications, including OpenGL apps" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url=$VCS_URL \
      org.label-schema.schema-version="1.0"
