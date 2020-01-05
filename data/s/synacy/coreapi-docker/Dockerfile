# Based on https://github.com/docker-library/openjdk/blob/master/8-jdk/Dockerfile, but using Debian Stretch instead.

FROM debian:stretch

##
# Install Java
##

RUN apt-get update && apt-get install -y --no-install-recommends bzip2 unzip xz-utils libterm-readline-perl-perl

RUN apt-get update && apt-get install -y openjdk-8-jdk ca-certificates-java

RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure

##
# Install git for circleci testing
##

RUN apt-get update && apt-get install -y git

##
# Install Core API dependencies
##

RUN apt-get update && apt-get install -y --no-install-recommends \
            libtiff-tools htmldoc libjpeg-progs netpbm \
            ghostscript=9.20~dfsg-3.2+deb9u1 imagemagick=8:6.9.7.4+dfsg-11+deb9u4 graphicsmagick=1.3.25-8 \
            qpdf=6.0.0-2 pdftk=2.02-4+b2 enscript

##
# Deploy custom written tools
##

ADD files/clean-pdf /usr/bin/
ADD files/setPageSizeA4.ps /etc/utbox/

##
# Deploy GraphicsMagick Configurations
##

ADD files/GraphicsMagick/*.mgk /etc/GraphicsMagick/

##
# Deploy custom fonts
##

# enable contrib sources so we can install mscorefonts
RUN sed -i 's/^deb http:\/\/deb.debian.org\/debian stretch main$/deb http:\/\/deb.debian.org\/debian stretch main contrib non-free/g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y --no-install-recommends ttf-mscorefonts-installer gsfonts

ADD files/fonts/*.TTF /usr/share/fonts/default/TrueType/
ADD files/fonts/*.ttf /usr/share/fonts/default/TrueType/
ADD files/fonts/*.pfa /usr/share/fonts/type1/gsfonts/

##
# Deploy advertised fonts
##

ADD files/advertised-fonts.txt /etc/utbox/

##
# Cleanup apt-get caches to remove bloat from the image
##

RUN rm -rf /var/lib/apt/lists/*

##
# Premade /tmp/ directories. Workaround for unrecognized directory on first time use
##
# DocumentConversion /tmp/ directory
RUN mkdir -p /tmp/faxes/convert
# TiffSender /tmp/ directory
RUN mkdir -p /tmp/ut/java/tiffarchiver

##
# Docker HealthCheck
##

HEALTHCHECK --interval=30s --retries=3 --timeout=30s CMD test `df -m / | tail -1 | awk '{print $4}'` -gt 512 || exit 1
