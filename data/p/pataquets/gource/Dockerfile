FROM gcc:4

# Build docs:
# https://github.com/acaudwell/Gource/blob/master/INSTALL

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install \
      bsdmainutils \
      libboost-filesystem-dev \
      libfreetype6-dev \
      libglew-dev \
      libglm-dev \
      libpcre3-dev \
      libpng12-dev \
      libsdl2-dev \
      libsdl2-image-dev \
  && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/

COPY . /src/gource/
WORKDIR /src/gource/

RUN \
  ./autogen.sh && \
  ./configure --help && \
  ./configure \
  && \
  make && \
  make install && \
  make clean

ENTRYPOINT [ "gource" ]
