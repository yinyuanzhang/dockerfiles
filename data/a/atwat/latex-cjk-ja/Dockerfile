FROM ubuntu:bionic

RUN sed -e \
  's/http:\/\/archive\.ubuntu\.com/http:\/\/us-east-1.ec2.archive.ubuntu.com/' \
  -i /etc/apt/sources.list

RUN apt-get update -y -qq \
    && apt-get -y install --no-install-recommends \
      ghostscript \
      lmodern \
      make \
      texlive \
      texlive-fonts-extra \
      texlive-fonts-recommended \
      texlive-lang-cjk \
      texlive-lang-japanese \
      texlive-latex-extra \
    && kanji-config-updmap-sys ipaex \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ARG MAKE_JOBS=-j1
RUN apt-get update -y -qq \
    && apt-get -y install --no-install-recommends \
      autoconf \
      gcc \
      git \
      libc-dev \
      libjpeg-turbo8-dev \
      wget \
    && cd /tmp \
    && git clone --depth=1 -b ghostpdl-9.28rc2 git://git.ghostscript.com/ghostpdl.git \
    && cd ghostpdl \
    && ./autogen.sh \
      CFLAGS="-O3 -march=ivybridge" \
      --prefix=/usr \
      --disable-cups \
      --disable-gtk \
      --with-memory-alignment=8 \
    && echo "parallel jobs: ${MAKE_JOBS}" \
    && make ${MAKE_JOBS} \
    && make install \
    && apt-get -y purge \
      autoconf \
      gcc \
      git \
      libc-dev \
      libjpeg-turbo8-dev \
      wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/ghostpdl


VOLUME /paper
WORKDIR /paper

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]
