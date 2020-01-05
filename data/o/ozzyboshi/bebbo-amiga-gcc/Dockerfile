# Docker image for building Bebbo's Amiga toolchain from https://github.com/bebbo/amiga-gcc
# The image also includes some useful libraries from amigaports

FROM ubuntu:18.04
MAINTAINER Ozzyboshi <gun101@email.it>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y install zip wget bison make git gcc g++ lhasa libgmp-dev libmpfr-dev libmpc-dev flex gettext texinfo rsync joe vim locate curl inetutils-ping libfreetype6-dev libsdl1.2-dev libncurses-dev
WORKDIR /root
RUN git clone https://github.com/bebbo/amiga-gcc.git
RUN cd amiga-gcc && make update && make all
ENV PATH="/opt/amiga/bin:${PATH}"
COPY ./SDL_image-pack /opt/amiga/SDL_image-pack
COPY ./zlib-package /opt/amiga/zlib-package
COPY ./SDL_mixer /opt/amiga/SDL_mixer
COPY ./libvorbis /opt/amiga/libvorbis
COPY ./libfreetype2 /opt/amiga/libfreetype2

# SDL libraries from Amigaports with AMMX support
RUN mkdir /opt/amiga/ammx
WORKDIR /opt/amiga/ammx
RUN git clone https://github.com/Amigaports/libSDL12
WORKDIR /opt/amiga/ammx/libSDL12
RUN make CPU=68080 PREFX=/opt/amiga
# end of SDL libraries from Amigaports with AMMX support

WORKDIR /opt/amiga/bin
CMD /opt/amiga/bin/m68k-amigaos-gcc
