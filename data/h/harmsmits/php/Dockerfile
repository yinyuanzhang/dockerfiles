FROM chialab/php:7.3-fpm

# Install Phalcon
RUN export APCU_VERSION=5.1.17 && \
    export PHALCON_EXT_PATH=php7/64bits && \
    export PHALCON_VERSION=3.4.4 && \
    export PSR_VERSION=0.6.0 && \
    export YAML_VERSION=2.0.4 && \
    export PQ_VERSION=2.1.5 && \
    export XDEBUG_VERSION=2.7.2 && \
    export RAPHF_VERSION=2.0.0 && \
    set -xe && \
    # Update packages
    apt-get update && \
    # Install LibYaml
    apt-get install -y libyaml-dev && \
    # Compile Phalcon
    curl -LO https://github.com/phalcon/cphalcon/archive/v${PHALCON_VERSION}.tar.gz && \
    tar xzf ${PWD}/v${PHALCON_VERSION}.tar.gz && \
    docker-php-ext-install -j $(getconf _NPROCESSORS_ONLN) ${PWD}/cphalcon-${PHALCON_VERSION}/build/${PHALCON_EXT_PATH} && \
    # Remove all temp files
    rm -r \
      ${PWD}/v${PHALCON_VERSION}.tar.gz \
      ${PWD}/cphalcon-${PHALCON_VERSION} && \
    # Install apcu, psr, yaml, and pq
    pecl install xdebug-${XDEBUG_VERSION} raphf-${RAPHF_VERSION} && \
    docker-php-ext-enable xdebug raphf && \
    pecl install apcu-${APCU_VERSION} psr-${PSR_VERSION} yaml-${YAML_VERSION} pq-${PQ_VERSION} && \
    docker-php-ext-enable apcu psr yaml pq