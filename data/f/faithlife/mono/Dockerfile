FROM ubuntu:bionic

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
  && apt-get install -y \
    ca-certificates \
    gnupg \
  && rm -rf /var/lib/apt/lists/*

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \
  && echo "deb https://download.mono-project.com/repo/ubuntu stable-bionic main" > /etc/apt/sources.list.d/mono-official-stable.list

RUN apt-get update \
  && apt-get install -y \
    mono-devel \
    nuget \
    tzdata \
  && rm -rf /var/lib/apt/lists/*
