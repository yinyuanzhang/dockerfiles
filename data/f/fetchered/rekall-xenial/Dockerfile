FROM ubuntu:xenial
MAINTAINER Corey Forman

USER root
RUN apt update && apt install -y \
  virtualenv \
  nano \
  git \
  python \
  python-pip \
  python-dev \
  libssl-dev \
  automake \
  make \
  gcc \
  flex \
  libtool \
  bison \
  ncurses-dev && \
  rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade setuptools pip wheel readline future==0.16.0 pybindgen pyaff4==0.26.post6 && \
  rm /usr/bin/pip && ln -s /usr/local/bin/pip /usr/bin/pip && \
  pip install fastchunking pyopenssl && \
  pip install -q distorm3 && \
  git clone https://github.com/VirusTotal/yara.git && \
  cd yara && \
  bash bootstrap.sh && \
  bash configure && \
  make && \
  make install && \
  make check && \
  echo "/usr/local/lib" >> /etc/ld.so.conf && \
  ldconfig && \
  cd .. && \
  rm -rf yara && \
  pip install rekall-agent rekall && \
  apt autoremove -y --purge && \
  apt clean -y


RUN groupadd -r nonroot && \
  useradd -r -g nonroot -d /home/nonroot -s /sbin/nologin -c "Nonroot User" nonroot && \
  mkdir /home/nonroot && \
  chown -R nonroot:nonroot /home/nonroot

USER nonroot
ENV HOME /home/nonroot
WORKDIR /home/nonroot
ENV USER nonroot
