FROM ubuntu

# So we can source (see http://goo.gl/oBPi5G)
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update

RUN apt install -y \
  python \
  python3 \
  python-pip \
  python3-pip \
  wget \
  curl \
  git \
  make \
  tmux \
  flex \
  bison \
  libreadline-dev \
  htop \
  screen \
  pandoc \
  aspell \
  poppler-utils \
  net-tools \
  g++ \
  sudo \
  psmisc \
  haproxy \
  nginx \
  yapf \
  rsync \
  tidy \
       avahi-daemon \
       expect \
       rlwrap \
       build-essential \
       mosquitto \
       mosquitto-clients \
       avahi-daemon \
       avahi-discover \
       avahi-utils \
       libnss-mdns \
       mdns-scan \
       sshpass \
  software-properties-common \
       vim \
       bup \
       inetutils-ping \
       lynx \
       telnet \
       git \
       subversion \
       ssh \
       m4 \
       latexmk \
       libpq5 \
       libpq-dev \
       build-essential \
       automake \
       gfortran \
       dpkg-dev \
       libssl-dev \
       imagemagick \
       libcairo2-dev \
       libcurl4-openssl-dev \
       graphviz \
       smem \
       python3-yaml \
       python3-matplotlib \
       python-matplotlib* \
       locales \
       locales-all \
       postgresql \
       postgresql-contrib \
       clang-format \
       yapf \
       yapf3 \
  aspell-* 

RUN wget -qO- https://deb.nodesource.com/setup_8.x | bash - && apt install -y nodejs
RUN npm install -g npm

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

## Xpra backend support -- we have to use the debs from xpra.org,
## Since the official distro packages are ancient.
RUN apt install -y xvfb websockify curl \
  && curl https://xpra.org/gpg.asc | apt-key add - \
  && echo "deb http://xpra.org/ bionic main" > /etc/apt/sources.list.d/xpra.list \
  && apt install -y xpra

## X11 apps to make x11 support useful.
## Will move this up in Dockerfile once stable.
RUN apt install -y \
       x11-apps \
       dbus-x11 \
       gnome-terminal \
       evince \
       mesa-utils \
       xdotool \
       xclip \
       x11-xkb-utils 

# User that the database, servers, etc. run under
RUN    adduser --quiet --shell /bin/bash --gecos "Sage user,101,," --disabled-password sage \
    && chown -R sage:sage /home/sage/

CMD ["/bin/bash"]
