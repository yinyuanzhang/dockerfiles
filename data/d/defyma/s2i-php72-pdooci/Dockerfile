FROM centos/s2i-base-centos7

# This image provides an Apache+PHP environment for running PHP
# applications.

EXPOSE 8080
EXPOSE 8443

# Description
# This image provides an Apache 2.4 + PHP 7.2 environment for running PHP applications.
# Exposed ports:
# * 8080 - alternative port for http

ENV PHP_VERSION=7.2 \
    PHP_VER_SHORT=72 \
    NAME=php \
    PATH=$PATH:/opt/rh/rh-php72/root/usr/bin

ENV SUMMARY="Platform for building and running PHP $PHP_VERSION applications" \
    DESCRIPTION="PHP $PHP_VERSION available as container is a base platform for \
building and running various PHP $PHP_VERSION applications and frameworks. \
PHP is an HTML-embedded scripting language. PHP attempts to make it easy for developers \
to write dynamically generated web pages. PHP also offers built-in database integration \
for several commercial and non-commercial database management systems, so writing \
a database-enabled webpage with PHP is fairly simple. The most common use of PHP coding \
is probably as a replacement for CGI scripts."

LABEL summary="${SUMMARY}" \
      description="${DESCRIPTION}" \
      io.k8s.description="${DESCRIPTION}" \
      io.k8s.display-name="Apache 2.4 with PHP ${PHP_VERSION}" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder,${NAME},${NAME}${PHP_VER_SHORT},rh-${NAME}${PHP_VER_SHORT}" \
      io.openshift.s2i.scripts-url="image:///usr/libexec/s2i" \
      io.s2i.scripts-url="image:///usr/libexec/s2i" \
      name="centos/${NAME}-${PHP_VER_SHORT}-centos7" \
      com.redhat.component="rh-${NAME}${PHP_VER_SHORT}-container" \
      version="${PHP_VERSION}" \
      help="For more information visit https://github.com/sclorg/s2i-${NAME}-container" \
      usage="s2i build https://github.com/sclorg/s2i-php-container.git --context-dir=${PHP_VERSION}/test/test-app centos/${NAME}-${PHP_VER_SHORT}-centos7 sample-server" \
      maintainer="SoftwareCollections.org <sclorg@redhat.com>"

# Install Apache httpd and PHP
RUN yum install -y centos-release-scl && \
    INSTALL_PKGS="rh-php72 rh-php72-php-devel rh-php72-php rh-php72-php-mysqlnd rh-php72-php-pgsql rh-php72-php-bcmath \
                  rh-php72-php-gd rh-php72-php-intl rh-php72-php-ldap rh-php72-php-mbstring rh-php72-php-pdo \
                  rh-php72-php-process rh-php72-php-soap rh-php72-php-opcache rh-php72-php-xml \
                  rh-php72-php-gmp rh-php72-runtime sclo-php72-php-pecl-xdebug rh-php72-php-pecl-apcu httpd24-mod_ssl" && \
    yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS --nogpgcheck && \
    rpm -V $INSTALL_PKGS && \
    yum clean all -y

ENV PHP_CONTAINER_SCRIPTS_PATH=/usr/share/container-scripts/php/ \
    APP_DATA=${APP_ROOT}/src \
    PHP_DEFAULT_INCLUDE_PATH=/opt/rh/rh-php72/root/usr/share/pear \
    PHP_SYSCONF_PATH=/etc/opt/rh/rh-php72 \
    PHP_HTTPD_CONF_FILE=rh-php72-php.conf \
    HTTPD_CONFIGURATION_PATH=${APP_ROOT}/etc/conf.d \
    HTTPD_MAIN_CONF_PATH=/etc/httpd/conf \
    HTTPD_MAIN_CONF_D_PATH=/etc/httpd/conf.d \
    HTTPD_VAR_RUN=/var/run/httpd \
    HTTPD_DATA_PATH=/var/www \
    HTTPD_DATA_ORIG_PATH=/opt/rh/httpd24/root/var/www \
    HTTPD_VAR_PATH=/opt/rh/httpd24/root/var \
    SCL_ENABLED=rh-php72

# Copy the S2I scripts from the specific language image to $STI_SCRIPTS_PATH
COPY ./s2i/bin/ $STI_SCRIPTS_PATH

# Copy extra files to the image.
COPY ./root/ /

# Reset permissions of filesystem to default values
RUN /usr/libexec/container-setup && rpm-file-permissions


##
## INSTALL OCI8, PDO_OCI

## re2c need forregenerate PHP parsers
RUN curl http://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/r/re2c-0.14.3-2.el7.x86_64.rpm --output re2c-0.14.3-2.el7.x86_64.rpm
RUN rpm -Uvh re2c-0.14.3-2.el7.x86_64.rpm
##	

#copy bahan oracle-instantclient12
#COPY ./bahan/instantclient_12_1 /opt/oracle/instantclient_12_1
COPY ./bahan/oci8-2.2.0 /opt/oci8-2.2.0
COPY ./bahan/pdo_oci /opt/pdo_oci

RUN yum install -y iproute /root/oracle-instantclient12* && yum clean all -y

RUN echo "/usr/lib/oracle/12.1/client64/lib" > /etc/ld.so.conf.d/oracle12.conf 
RUN ldconfig 

RUN cd /opt/oci8-2.2.0; \
	phpize; \
	./configure; \
	make && make install

RUN echo "extension=oci8" > /etc/opt/rh/rh-php72/php.d/20-oci8.ini

RUN cd /opt/pdo_oci; \
	phpize ORACLE_HOME=/usr/lib/oracle/12.1/client64/lib; \
	./configure --with-pdo-oci=instantclient,/usr/lib/oracle/12.1/client64/lib,12.1; \
	make && make install

RUN echo "extension=pdo_oci" > /etc/opt/rh/rh-php72/php.d/99-pdo_oci.ini


## END INSTALL OCI8 PDO_OCI


# In order to drop the root user, we have to make some directories world
# writeable as OpenShift default security model is to run the container under
# random UID.
RUN sed -i -f /opt/app-root/etc/httpdconf.sed /opt/rh/httpd24/root/etc/httpd/conf/httpd.conf && \
    echo "IncludeOptional /opt/app-root/etc/conf.d/*.conf" >> /opt/rh/httpd24/root/etc/httpd/conf/httpd.conf && \
    sed -i '/php_value session.save_path/d' /opt/rh/httpd24/root/etc/httpd/conf.d/rh-php72-php.conf && \
    head -n151 /opt/rh/httpd24/root/etc/httpd/conf/httpd.conf | tail -n1 | grep "AllowOverride All" || exit && \
    mkdir -p /tmp/sessions && \
    chown -R 1001:0 /opt/app-root /tmp/sessions && \
    chmod -R a+rwx /tmp/sessions && \
    chmod -R ug+rwx /opt/app-root && \
    chmod -R a+rwx /etc/opt/rh/rh-php72 && \
chmod -R a+rwx /opt/rh/httpd24/root/var/run/httpd


USER 1001

# Set the default CMD to print the usage of the language image
CMD $STI_SCRIPTS_PATH/usage
