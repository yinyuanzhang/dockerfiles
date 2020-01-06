FROM ubuntu:latest 
MAINTAINER Oliver Makrs <oly@digitaloctave.com>

ENV DISPLAY :0

RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y \
  git \
  libblas-dev liblapack-dev libatlas-base-dev gfortran \
  libgl1-mesa-dri \
  net-tools \
  python-pip \
  sudo \
  tint2 \
  mesa-utils \
  x11-xserver-utils \
  xinit \
  xserver-xorg-video-dummy \
  xserver-xorg-input-void && \
  apt remove -y python-pip && \
  apt -y clean

COPY etc /etc
COPY start.sh /start.sh

RUN useradd -m -s /bin/bash user
USER user

RUN cp /etc/skel/.xinitrc /home/user/
USER root
RUN echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/user

WORKDIR /app

CMD ["bash"]
ENTRYPOINT ["/start.sh"]
