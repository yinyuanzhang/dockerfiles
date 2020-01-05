FROM centos:7
MAINTAINER "devops" <it-devops@pixartprinting.com>
LABEL maintainer=it-devops@pixartprinting.com

ENV TZ=Europe/Rome

COPY pixart.pem /etc/pki/ca-trust/source/anchors/

RUN	yum -y install \
    ca-certificates && \
    update-ca-trust extract && \
    rm -fr /var/cache/yum

COPY repos/*.repo /etc/yum.repos.d/

RUN	rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    rpm --import http://rpms.famillecollet.com/RPM-GPG-KEY-remi && \
    rpm --import http://download.newrelic.com/548C16BF.gpg && \
    rpm --import https://archive.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7 && \
    rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm && \
    rpm -Uvh http://yum.newrelic.com/pub/newrelic/el5/x86_64/newrelic-repo-5-3.noarch.rpm && \
    curl -o /etc/yum.repos.d/newrelic-infra.repo https://download.newrelic.com/infrastructure_agent/linux/yum/el/7/x86_64/newrelic-infra.repo && \
    yum-config-manager --enable extras && \
    yum-config-manager --enable epel && \
    yum-config-manager --disable remi && \
    yum-config-manager --disable remi-php55 && \
    yum-config-manager --enable remi-php56 && \
    yum-config-manager --disable remi-php70 && \
    yum-config-manager --disable remi-php71

# Install packages
RUN	yum -y update && \
    yum -y install \
    composer \
    unzip \
    deltarpm \
    bind-utils \
    lsof \
    git \
    nginx \
    supervisor \
    php \
    php-cli \
    php-fpm \
    php-bcmath \
    php-common \
    php-gd \
    php-intl \
    php-mbstring \
    php-mcrypt \
    php-mysqli \
    php-pdo \
    php-soap \
    php-xml \
    php-pecl-apcu \
    php-pecl-imagick \
    php-pecl-zendopcache \
    php-pecl-redis \
    php-pecl-memcached \
    php-pecl-msgpack \
    newrelic-php5 \
    php-pecl-xdebug \
    awscli \
    mysql \
    newrelic-infra && \
    NR_INSTALL_USE_CP_NOT_LN=1 NR_INSTALL_SILENT=1 newrelic-install install && \
    rm -fr /var/cache/yum

COPY $DOCKER_ARTIFACT_DIR/supervisord/supervisord.conf /etc/supervisord.conf
COPY $DOCKER_ARTIFACT_DIR/supervisord/stop.sh /bin/

CMD ["/usr/bin/supervisord", "-c",  "/etc/supervisord.conf"]
EXPOSE 80