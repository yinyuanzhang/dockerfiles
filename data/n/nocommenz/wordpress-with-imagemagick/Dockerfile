FROM wordpress:latest

ENV IMAGE_MAGICK_VERSION="7.0.8-35"
ENV WEBP_VERSION="1.0.0"

# Compile libwebp from source
WORKDIR /
RUN apt-get update \
  && apt-get install -y apt-utils apt-transport-https libjpeg-dev libpng-dev wget
RUN wget https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-${WEBP_VERSION}.tar.gz \
  && tar xvzf libwebp-${WEBP_VERSION}.tar.gz
# TODO: Find solution for cd to folder with alternative version
RUN ls
WORKDIR /libwebp-${WEBP_VERSION}
RUN ./configure
RUN make
RUN make install

# Compile imagemagick from source, configured with webp
WORKDIR /
# RUN apt build-dep imagemagick
# RUN apt-get update && apt-get build-dep imagemagick -y
# RUN wget https://imagemagick.org/download/ImageMagick.tar.gz # latest version
# See more at https://www.imagemagick.org/download/releases/
RUN wget https://www.imagemagick.org/download/releases/ImageMagick-${IMAGE_MAGICK_VERSION}.tar.gz
RUN tar xvzf ImageMagick-${IMAGE_MAGICK_VERSION}.tar.gz
# TODO: Find solution for cd to folder with alternative version
WORKDIR /ImageMagick-${IMAGE_MAGICK_VERSION}
RUN pwd
RUN ls -a
RUN ./configure --with-webp=yes
RUN make
RUN make install
RUN ldconfig /usr/local/lib
RUN identify -version
# RUN make check

# Install extension with pecl
RUN apt-get install -y imagemagick gcc libmagickwand-dev
RUN pecl install imagick
RUN echo "extension=imagick.so" >> /usr/local/etc/php/php.ini
# RUN service apache2 restart

WORKDIR /var/www/html

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["apache2-foreground"]