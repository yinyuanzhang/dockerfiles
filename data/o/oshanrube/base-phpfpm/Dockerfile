# phpfpm
FROM oshanrube/base

# TODO: Put the maintainer name in the image metadata
MAINTAINER Oshan Rube <oshanrube@gmail.com>

# TODO: Rename the builder environment variable to inform users about application you provide them
ENV BUILDER_VERSION 1.0
ENV PHPFPM_VERSION=5.3

# TODO: Set labels used in OpenShift to describe the builder image
LABEL io.k8s.description="Base for building phpfpm" \
      io.k8s.display-name="builder phpfpm 0.0.1" \
      io.openshift.expose-services="9000:http" \
      io.openshift.tags="builder,0.0.1,phpfpm,etc."

# TODO: Install required packages here:
RUN dnf -y install  php-pear ImageMagick ImageMagick-devel ImageMagick-perl \
	php php-fpm php-mbstring php-mcrypt php-curl php-xsl php-gd php-mysql php-gd \
	php-xml php-soap php-intl php-openssl php-pecl-memcache \
	php-opcache php-gd php-devel php-bcmath php-dom php-zip && \
	dnf -y clean all
RUN pecl install imagick

COPY  ["config/php-fpm.conf", "/etc/php-fpm.conf"]
COPY  ["config/www.conf", "/etc/php-fpm.d/www.conf"]
COPY  ["config/php.ini", "/etc/php.ini"]

# TODO: Copy the S2I scripts to /usr/local/s2i, since openshift/base-centos7 image sets io.openshift.s2i.scripts-url label that way, or update that label
COPY ./.s2i/bin/ $STI_SCRIPTS_PATH

# TODO: Drop the root user and make the content of /opt/app-root owned by user 1001
RUN mkdir -p /var/www/html && chmod -R a+rwx /var/www/html && chown -R 1001:0 /var/www/html
RUN chown -R 1001:0 /var/lib/php/session

# logs
RUN ln -sf /dev/stdout /var/log/php-fpm/access.log
RUN ln -sf /dev/stderr /var/log/php-fpm/error.log

# TODO: Set the default port for applications built using this image
EXPOSE 9000

# TODO: Set the default CMD for the image
CMD $STI_SCRIPTS_PATH"/usage"
