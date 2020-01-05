FROM ruby:2.6.5

ENV DISCOURSE_VERSION=2.3.6
ENV PG_MAJOR 11

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    TERM=xterm-256color \
    DEBIAN_FRONTEND=noninteractive

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
	apt-get -qq update && apt-get -qq install --upgrade -y nodejs > /dev/null && \
	npm install --global webpack yarn semver svgo && \
	apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD install-imagemagick /tmp/install-imagemagick
RUN /tmp/install-imagemagick \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/ImageMagick-*/policy.xml

# Validate install
RUN ruby -Eutf-8 -e "v = \`convert -version\`; %w{png tiff jpeg freetype}.each { |f| unless v.include?(f); STDERR.puts('no ' + f +  ' support in imagemagick'); exit(-1); end }"

ADD install-pngcrush /tmp/install-pngcrush
RUN /tmp/install-pngcrush \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD install-gifsicle /tmp/install-gifsicle
RUN /tmp/install-gifsicle \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD install-pngquant /tmp/install-pngquant
RUN /tmp/install-pngquant \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN apt-get -qq update \
  && apt-get -qq install --upgrade -y --no-install-recommends \
    brotli \
    build-essential \
    gawk \
    gifsicle \
    git \
    jhead \
    jpegoptim \
    libcurl4-openssl-dev \
    libpq-dev \
    libreadline-dev \
    libssl-dev \
    libtcmalloc-minimal4 \
    libtool \
    libunwind-dev \
    libxml2-dev \
    libxslt-dev \
    libyaml-dev \
    optipng \
    parallel \
    postgresql-client-${PG_MAJOR} \
    postgresql-contrib \
    rsync \
    sudo \
    vim \
    wget \
    > /dev/null \
  && apt-get -qq clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN addgroup --gid 1000 discourse \
    && adduser --system --uid 1000 --ingroup discourse --shell /bin/bash discourse \
    && cd /home/discourse \
    && mkdir -p tmp \
    && git clone --branch v${DISCOURSE_VERSION} https://github.com/discourse/discourse.git \
    && chown -R discourse:discourse . \
    && cd /home/discourse/discourse \
    && git remote set-branches --add origin tests-passed

WORKDIR /home/discourse/discourse

USER discourse:discourse

ENV DISCOURSE_SERVE_STATIC_ASSETS=true \
    RAILS_ENV=production

RUN bundle config build.nokogiri --use-system-libraries \
    && bundle install --deployment --without test development --retry 3 --jobs 4 \
    && bundle exec rake maxminddb:get \
    && find ./vendor/bundle -name tmp -type d -exec rm -rf {} +

ENV RAILS_LOG_TO_STDOUT=true \
    RUBY_GC_HEAP_GROWTH_MAX_SLOTS=40000 \
    RUBY_GC_HEAP_INIT_SLOTS=400000 \
    RUBY_GC_HEAP_OLDOBJECT_LIMIT_FACTOR=1.5 \
    RUBY_GLOBAL_METHOD_CACHE_SIZE=131072 \
    SPROCKETS_CONCURRENT=1 \
    UNICORN_BIND_ALL=true

COPY config/environments/production.rb config/environments/
COPY config/unicorn.conf.rb config/
