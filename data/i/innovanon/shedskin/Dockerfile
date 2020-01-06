FROM python:2

RUN                             \
  apt update                 && \
  apt install -y   \
    g++            \
    libpcre++-dev  \
    python-all-dev \
    libgc-dev                && \
  apt install -y shedskin    && \
  apt clean                  && \
  rm -rf                 \
    /tmp/*               \
    /var/lib/apt/lists/* \
    /var/cache/apt/*

#RUN git clone https://github.com/shedskin/shedskin
#RUN cd shedskin && python setup.py install
