FROM ubuntu:xenial

RUN apt-get update && apt-get install -y \
      build-essential \
      curl \
      gdb \
      git \
      inetutils-ping \
      libffi-dev \
      libssl-dev \
      net-tools \
      netcat \
      python-pip \
      python2.7 \
      tcpdump \
      vim \
      ;

RUN pip install --upgrade pip \
      capstone \
      filebytes \
      pwntools \
      ropper \
      ;

WORKDIR /root/github

RUN git clone --recursive https://github.com/jiulongw/dotfiles dotfiles && \
      dotfiles/setup_bash && \
      dotfiles/setup_vim

RUN git clone --recursive https://github.com/longld/peda.git peda && \
      echo "source /root/github/peda/peda.py" >> /root/.gdbinit

WORKDIR /root

