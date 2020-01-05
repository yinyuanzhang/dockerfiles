FROM bitnami/php-fpm:7.2

ENV DEBIAN_FRONTEND noninteractive

COPY php.ini /opt/bitnami/php/etc/conf.d/custom.ini
COPY docker-entrypoint.sh /

RUN chmod +x /docker-entrypoint.sh && \
  mkdir -p /var/php/sessions && \
  mkdir -p /var/php/sessions && \
  mkdir -p /var/log/app && \
  apt-get -y update --fix-missing && \
  # Install important libraries
  install_packages acl nodejs git curl openssl && \
  # Install wkhtmltopdf
  install_packages zlib1g fontconfig libfreetype6 libx11-6 libxext6 libxrender1 xfonts-75dpi xfonts-base && \
  wget -qP /tmp https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb && \
  apt-get install -fy /tmp/wkhtmltox_0.12.5-1.stretch_amd64.deb && \
  # Install useful tools
  install_packages nano wget less && \
  # ImageMagick
  install_packages \
  # runtime requirements for ImageMagick PHP extension
  fontconfig-config fonts-dejavu-core imagemagick-6-common \
  libfftw3-double3 libfontconfig1 libglib2.0-0 libgomp1 libjbig0 \
  liblcms2-2 liblqr-1-0 libltdl7 libmagickcore-6.q16-3 \
  libmagickwand-6.q16-3 libopenjp2-7 libtiff5 libx11-6 libx11-data libxau6 \
  libxcb1 libxdmcp6 libxext6 \
  # compile-time requirements for ImageMagick PHP extension
  gcc make autoconf libc-dev pkg-config libmagickwand-dev && \
  # Install imagick php extension and enable it
  # At one point in the installer, a default value should be used, which
  # requires the user to press enter. "echo" simulates this interaction
  echo "" | pecl install imagick && \
  echo "" >> /opt/bitnami/php/etc/php.ini && \
  echo "extension=imagick\n" > /opt/bitnami/php/etc/conf.d/imagemagick.ini && \
  echo "[www]\nenv[MAGICK_CODER_MODULE_PATH]='/usr/lib/x86_64-linux-gnu/ImageMagick-6.9.7/modules-Q16/coders'" > /opt/bitnami/php/etc/php-fpm.d/imagemagick.conf && \
  # Clean up
  apt-get -qq -y remove --auto-remove gcc make autoconf libc-dev pkg-config libmagickwand-dev && \
  rm -rf /usr/include/* && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  # Config tweaks
  sed -i 's/;access.log = log/access.log = logs/' /opt/bitnami/php/etc/php-fpm.d/www.conf && \
  sed -i 's/;access.format/access.format/' /opt/bitnami/php/etc/php-fpm.d/www.conf && \
  sed -i 's|;chdir = /var/www|chdir = /app/public_html|' /opt/bitnami/php/etc/php-fpm.d/www.conf

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD [ "php-fpm", "-F", "--pid", "/opt/bitnami/php/tmp/php-fpm.pid", "-y", "/opt/bitnami/php/etc/php-fpm.conf" ]
VOLUME [ "/var/php/sessions", "/var/log/app" ]