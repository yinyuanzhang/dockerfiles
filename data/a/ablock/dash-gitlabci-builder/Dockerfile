FROM ubuntu:bionic

# Build and base stuff
# (zlib1g-dev and libssl-dev are needed for the Qt host binary builds, but should not be used by target binaries)
# We split this up into multiple RUN lines as we might need to retry multiple times on Travis. This way we allow better
# cache usage.
RUN apt-get update && apt-get install -y wget unzip git && apt-get clean && rm -fr /var/cache/apt/*
RUN apt-get update && apt-get install -y g++ && apt-get clean && rm -fr /var/cache/apt/*
RUN apt-get update && apt-get install -y autotools-dev libtool m4 automake autoconf pkg-config && apt-get clean && rm -fr /var/cache/apt/*
RUN apt-get update && apt-get install -y zlib1g-dev libssl1.0-dev curl ccache bsdmainutils cmake && apt-get clean && rm -fr /var/cache/apt/*
RUN apt-get update && apt-get install -y python3 python3-dev python3-pip python3-zmq && apt-get clean && rm -fr /var/cache/apt/*

RUN dpkg --add-architecture i386

# linux32 & linux64
RUN apt-get update && apt-get install -y g++-multilib gcc g++ && apt-get clean && rm -fr /var/cache/apt/*
# arm
RUN apt-get update && apt-get install -y g++-arm-linux-gnueabihf && apt-get clean && rm -fr /var/cache/apt/*
# win32 & win64
RUN apt-get update && apt-get install -y g++-mingw-w64-i686 g++-mingw-w64-x86-64 nsis wine64 wine-stable wine32 bc && apt-get clean && rm -fr /var/cache/apt/*
# mac
RUN apt-get update && apt-get install -y cmake imagemagick libcap-dev librsvg2-bin libz-dev libbz2-dev libtiff-tools && apt-get clean && rm -fr /var/cache/apt/*

RUN apt-get update && apt-get dist-upgrade -y && apt-get clean && rm -fr /var/cache/apt/*