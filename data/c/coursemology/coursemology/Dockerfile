FROM ruby:2.5 as builder

# Taken from https://github.com/plataformatec/engine-image-optim/blob/master/Dockerfile
# which is based on https://github.com/toy/image_optim_pack/pull/5
ARG JPEGOPTIM_VERSION=1.4.3
ARG PNGCRUSH_VERSION=1.8.11
ARG ZOPFLI_VERSION=1.0.1
ARG ADVANCECOMP_VERSION=1.20
ARG JHEAD_VERSION=3.00
ARG GIFSICLE_VERSION=1.88
ARG OPTIPNG_VERSION=0.7.5
ARG PNGQUANT_VERSION=2.5.2
ARG JPEGARCHIVE_VERSION=2.1.1
ARG MOZJPEG_VERSION=3.1
ARG IJG_VERSION=9a
ARG PNGOUT_VERSION=20150319
ARG SKIP_IMAGE_OPTIM_PACK=1

WORKDIR /tmp

# Install dependencies needed building assets and precompile.
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && apt-get update && apt-get install apt-transport-https \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
  && curl -sL https://deb.nodesource.com/setup_10.x | bash - \
  && apt-get install -y nodejs yarn nasm \
  # advancecomp
  && curl -L -O https://github.com/amadvance/advancecomp/releases/download/v$ADVANCECOMP_VERSION/advancecomp-$ADVANCECOMP_VERSION.tar.gz \
  && tar zxf advancecomp-$ADVANCECOMP_VERSION.tar.gz \
  && cd advancecomp-$ADVANCECOMP_VERSION \
  && ./configure && make && make install \
  && cd .. \
  # gifsicle
  && curl -O https://www.lcdf.org/gifsicle/gifsicle-$GIFSICLE_VERSION.tar.gz \
  && tar zxf gifsicle-$GIFSICLE_VERSION.tar.gz \
  && cd gifsicle-$GIFSICLE_VERSION \
  && ./configure && make && make install \
  && cd .. \
  # jhead
  && curl -O http://www.sentex.net/~mwandel/jhead/jhead-$JHEAD_VERSION.tar.gz \
  && tar zxf jhead-$JHEAD_VERSION.tar.gz \
  && cd jhead-$JHEAD_VERSION \
  && make && make install \
  && cd .. \
  # jpegoptim
  && curl -O https://www.kokkonen.net/tjko/src/jpegoptim-$JPEGOPTIM_VERSION.tar.gz \
  && tar zxf jpegoptim-$JPEGOPTIM_VERSION.tar.gz \
  && cd jpegoptim-$JPEGOPTIM_VERSION \
  && ./configure && make && make install \
  && cd .. \
  # jpeg-recompress (from jpeg-archive along with mozjpeg dependency)
  && curl -L -O https://github.com/mozilla/mozjpeg/archive/v$MOZJPEG_VERSION.tar.gz \
  && tar zxf v$MOZJPEG_VERSION.tar.gz \
  && cd mozjpeg-$MOZJPEG_VERSION \
  && autoreconf -fiv && ./configure && make && make install \
  && cd .. \
  && curl -L -O https://github.com/danielgtaylor/jpeg-archive/archive/$JPEGARCHIVE_VERSION.tar.gz \
  && tar zxf $JPEGARCHIVE_VERSION.tar.gz \
  && cd jpeg-archive-$JPEGARCHIVE_VERSION \
  && make && make install \
  && cd .. \
  # jpegtran (from Independent JPEG Group)
  && curl -O http://www.ijg.org/files/jpegsrc.v$IJG_VERSION.tar.gz \
  && tar zxf jpegsrc.v$IJG_VERSION.tar.gz \
  && cd jpeg-$IJG_VERSION \
  && ./configure && make && make install \
  && cd .. \
  # optipng
  && curl -L -O http://downloads.sourceforge.net/project/optipng/OptiPNG/optipng-$OPTIPNG_VERSION/optipng-$OPTIPNG_VERSION.tar.gz \
  && tar zxf optipng-$OPTIPNG_VERSION.tar.gz \
  && cd optipng-$OPTIPNG_VERSION \
  && ./configure && make && make install \
  && cd .. \
  # pngcrush
  && curl -L -O http://downloads.sourceforge.net/project/pmt/pngcrush/$PNGCRUSH_VERSION/pngcrush-$PNGCRUSH_VERSION.tar.gz \
  && tar zxf pngcrush-$PNGCRUSH_VERSION.tar.gz \
  && cd pngcrush-$PNGCRUSH_VERSION \
  && make && cp -f pngcrush /usr/local/bin \
  && cd .. \
  # pngout (binary distrib)
  && curl -O http://static.jonof.id.au/dl/kenutils/pngout-$PNGOUT_VERSION-linux-static.tar.gz \
  && tar zxf pngout-$PNGOUT_VERSION-linux-static.tar.gz \
  && cd pngout-$PNGOUT_VERSION-linux-static \
  && cp -f x86_64/pngout-static /usr/local/bin/pngout \
  && cd .. \
  # pngquant
  && curl -L -O http://pngquant.org/pngquant-$PNGQUANT_VERSION-src.tar.bz2 \
  && tar xjf pngquant-$PNGQUANT_VERSION-src.tar.bz2 \
  && cd pngquant-$PNGQUANT_VERSION \
  && ./configure && make && make install \
  && cd .. \
  # svgo
  && npm install -g svgo \
  # refresh library cache, as libjpeg was installed into /usr/local/lib for jpegtran
  && ldconfig \
  && npm install node-sass

RUN mkdir -p /app
WORKDIR /app

# Main build script to patch open source version to production readiness.
COPY build-cm2.sh /app

# Copy source code folders and local patches/files folders to build image.
COPY coursemology2 /app/coursemology2
COPY coursemology-theme /app/coursemology-theme
COPY patches /app/patches
COPY files /app/files

ENV AWS_ACCESS_KEY_ID="access" AWS_SECRET_ACCESS_KEY="secret" AWS_REGION="ap-southeast-1" \
    AWS_BUCKET="coursemology2" BUNDLE_APP_CONFIG=/app/coursemology2/.bundle

RUN /app/build-cm2.sh

FROM ruby:2.5 AS coursemology

RUN useradd -d /app -u 10000 app \
# We need to add app to group uid 999 (corresponding to the Docker gid in the host)
  && addgroup -gid 999 --system docker && adduser app docker

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
  && apt-get install -y ghostscript nodejs imagemagick

WORKDIR /app/coursemology2
COPY --from=builder /app/coursemology2 .
RUN mkdir -p tmp/pids tmp/sockets log
# Only give app user ownership of the files/folders it needs.
RUN chown -R app /app/coursemology2/tmp /app/coursemology2/Gemfile.lock /app/coursemology2/log

ENV BUNDLE_APP_CONFIG=/app/coursemology2/.bundle RAILS_ENV=production

USER app
