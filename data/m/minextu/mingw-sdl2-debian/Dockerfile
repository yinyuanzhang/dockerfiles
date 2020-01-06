FROM minextu/mingw-debian:latest
MAINTAINER minextu

# debian stretch sdl versions
ENV SDL_VERSION 2.0.5
ENV SDL_IMAGE_VERSION 2.0.1
ENV SDL_TTF_VERSION 2.0.14

# install mingw-sdl2
RUN cd /tmp && \
    wget http://libsdl.org/release/SDL2-devel-${SDL_VERSION}-mingw.tar.gz && \
    tar -zxf SDL2-devel-${SDL_VERSION}-mingw.tar.gz && \
    cd SDL2-${SDL_VERSION} && \
    # Update mingw path to /usr (TODO: path cross-tools was removed in newer versions)
    sed -i "s#CROSS_PATH := /usr/local/cross-tools#CROSS_PATH := /usr#" Makefile && \
    make install cross &&\
    rm -r /tmp/*

# install mingw-sdl2_image
RUN cd /tmp && \
    wget http://www.libsdl.org/projects/SDL_image/release/SDL2_image-devel-${SDL_IMAGE_VERSION}-mingw.tar.gz && \
    tar -zxf SDL2_image-devel-${SDL_IMAGE_VERSION}-mingw.tar.gz && \
    cd SDL2_image-${SDL_IMAGE_VERSION} && \
    # Update mingw path to /usr (TODO: path cross-tools was removed in newer versions)
    sed -i "s#CROSS_PATH := /usr/local/cross-tools#CROSS_PATH := /usr#" Makefile && \
    make install cross &&\
    rm -r /tmp/*

# install mingw-sdl2_ttf
RUN cd /tmp && \
    wget http://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-devel-${SDL_TTF_VERSION}-mingw.tar.gz && \
    tar -zxf SDL2_ttf-devel-${SDL_TTF_VERSION}-mingw.tar.gz && \
    cd SDL2_ttf-${SDL_TTF_VERSION} && \
    # Update mingw path to /usr (TODO: path cross-tools will get removed in newer versions)
    sed -i "s#CROSS_PATH := /usr/local/cross-tools#CROSS_PATH := /usr#" Makefile && \
    make install cross &&\
    rm -r /tmp/*
    
CMD /bin/bash
