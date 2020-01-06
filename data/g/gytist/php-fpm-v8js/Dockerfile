FROM php:7.3.1-fpm

LABEL maintainer="Gytis Tamulynas <GytisT1@gmail.com>"
LABEL version="1.1.0"
LABEL description="PHP 7.3.1 FPM with v8 7.4 + v8js and some other essentials"
 
# Update & install essentials
RUN apt-get update && apt-get install -y --no-install-recommends \
    mysql-client \
    git \
    build-essential \
    curl \
    python \
    libglib2.0-dev \
	patchelf \
    && docker-php-ext-install pdo_mysql bcmath \
    && cd /tmp \
    \
    && git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git --progress --verbose \
    && export PATH="$PATH:/tmp/depot_tools" \
    \
    && fetch v8 \
    && cd v8 \
    && git checkout 7.4.195 \
    && gclient sync \
    \
    && tools/dev/v8gen.py -vv x64.release -- \
	binutils_path=\"/usr/bin\" \
    target_os=\"linux\" \
    target_cpu=\"x64\" \
    v8_target_cpu=\"x64\" \
    v8_use_external_startup_data=false \
    is_official_build=true \
    is_component_build=true \
    is_cfi=false \
    is_clang=false \
    use_custom_libcxx=false \
    use_sysroot=false \
    use_gold=false \
    use_allocator_shim=false \
    treat_warnings_as_errors=false \
    symbol_level=0 \
    \
    && ninja -C out.gn/x64.release/ \
    && mkdir -p /opt/libv8-7.4/lib \
    && mkdir /opt/libv8-7.4/include \
    && cp out.gn/x64.release/lib*.so out.gn/x64.release/icudtl.dat \
	/opt/libv8-7.4/lib/ \
    && cp -R include/* /opt/libv8-7.4/include/ \
	&& for A in /opt/libv8-7.4/lib/*.so; do patchelf --set-rpath '$ORIGIN' $A;done \
    \
    && cd /tmp \
    && git clone https://github.com/phpv8/v8js.git \
    && cd v8js \
    && git checkout php7 \
    && phpize \
    && ./configure --with-v8js=/opt/libv8-7.4 \
    && export NO_INTERACTION=1 \
    && make \
	&& make test \
    && make install \
    && docker-php-ext-enable v8js \
    \
    && rm -rf /tmp/* \
	&& apt-get remove -y git build-essential curl python libglib2.0-dev \
	&& apt-get autoremove -y \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*
