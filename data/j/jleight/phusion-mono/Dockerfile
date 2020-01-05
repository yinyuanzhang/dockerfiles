FROM phusion/baseimage:latest
MAINTAINER Jonathon Leight <jonathon.leight@jleight.com>

ENV MONO_VERSION wheezy/snapshots/3.10.0
ENV MONO_REPO http://download.mono-project.com/repo/debian
ENV MONO_APT_LIST /etc/apt/sources.list.d/mono-xamarin.list

RUN set -x \
  && apt-key adv \
    --keyserver keyserver.ubuntu.com \
    --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \
  && echo "deb ${MONO_REPO} ${MONO_VERSION} main" > ${MONO_APT_LIST} \
  && apt-get update \
  && apt-get install -y mono-devel fsharp mono-vbnc nuget \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/*