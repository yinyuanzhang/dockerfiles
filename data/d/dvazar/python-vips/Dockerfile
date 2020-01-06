FROM python:3.6.9-slim-stretch

# libvips settings
ARG LIBVIPS_VERSION=8.8.1
ARG PYVIPS_VERSION=2.1.2


# Install libvips library
RUN apt-get update -y \
 && apt-get install -y \
  wget \
  build-essential \
  pkg-config \
  glib2.0-dev \
  libmagickwand-dev \
  libmagic-dev \
  libfftw3-dev \
  libpoppler-glib-dev \
  libexif-dev \
  libgif-dev \
  librsvg2-dev \
  libexpat1-dev \
  libtiff5-dev \
  libjpeg62-turbo-dev \
  libgsf-1-dev \
  libxml2-dev \
  liborc-0.4-dev \
  libpng-dev \
  libwebp-dev \
  libopenexr-dev \
  liblcms2-dev \
  libcurl4-nss-dev \
 && apt-get clean \
 && wget -O vips.tar.gz "https://github.com/libvips/libvips/releases/download/v${LIBVIPS_VERSION}/vips-${LIBVIPS_VERSION}.tar.gz" \
 && mkdir libvips \
 && tar xvz -f vips.tar.gz -C libvips --strip-components=1 \
 && cd libvips \
 && ./configure \
 && make install \
 && cd .. \
 && rm -rf libvips vips.tar.gz \
 && ldconfig \
 && pip --no-cache-dir install pyvips==${PYVIPS_VERSION} \
 && apt-get install -y fonts-wqy-zenhei \
 && apt-get remove -y \
  build-essential \
  wget \
 && apt-get autoremove -y \
 && apt-get autoclean \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
