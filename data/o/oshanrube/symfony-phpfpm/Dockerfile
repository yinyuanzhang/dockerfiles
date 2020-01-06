# symfony
FROM oshanrube/base-phpfpm

# TODO: Put the maintainer name in the image metadata
MAINTAINER Oshan Rube <oshanrube@gmail.com>

# TODO: Set labels used in OpenShift to describe the builder image
LABEL io.k8s.description="Platform for building symfony phpfpm" \
      io.k8s.display-name="builder phpfpm 0.0.1" \
      io.openshift.expose-services="9000:http" \
      io.openshift.tags="builder,0.0.1,phpfpm,etc."

# install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN chmod -R a+rwx /opt/app-root/src/.composer && chown -R 1001:0 /opt/app-root/src/.composer

# install node
RUN dnf -y install nodejs && dnf -y clean all

COPY  ["config/www.conf", "/etc/php-fpm.d/www.conf"]
COPY  ["config/php.ini", "/etc/php.ini"]

# TODO: Copy the S2I scripts to /usr/local/s2i, since openshift/base-centos7 image sets io.openshift.s2i.scripts-url label that way, or update that label
COPY ./.s2i/bin/ $STI_SCRIPTS_PATH

# This default user is created in the openshift/base-centos7 image
USER 1001
