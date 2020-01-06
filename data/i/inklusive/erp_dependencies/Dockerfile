# Match Debian version as closely as possible to pg-[blue,green].inklusive.fr
FROM ruby:2.4-buster

# git for git-ls and ruby gems, so I can run 'bundle install' inside a container
#
# Dependency: libicu-dev (system library)
# libicu-dev: for charlock_holmes gem (encoding detector)
#
# poppler-utils: pdftotext
#
# graphviz: rails erd
#
# wicked_pdf gem dependencies
# Don't use the apt-get repos which require an X server, use this .deb instead (for ubuntu 14.04)
# See: http://wkhtmltopdf.org/downloads.html
# xfonts-base xfonts-75dpi
#
# openjdk-8-jre libpostgresql-jdbc-java: SchemaSpy dependency (ERD generation tool)
#
# imagemagick: for image uploading
#
# locales-all is mandatory for tmux (requires UTF8 locale set), alternative to locale-gen??
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get upgrade -y && apt-get install -y \
                    xfonts-base \
                    xfonts-75dpi \
                    postgresql-client \
                    libsqlite3-dev \
                    jpegoptim \
                    optipng \
                    git \
                    libicu-dev \
                    poppler-utils \
                    graphviz \
                    openjdk-11-jre libpostgresql-jdbc-java \
                    imagemagick \
                    chromium \
                    x11-apps \
                    libgconf-2-4 \
                    unzip \
                    tmux \
                    less \
                    man \
                    rsync \
                    locales-all \
                    && rm -rf /var/lib/apt/lists/*

# nodejs package does not provide npm in Debian stretch
# wktohtml needs to be upgraded bit by bit (keeping Debian stretch version above for easier later switch)
# 2018-01-17 : Removing Debian stretch version because WickedPdf.new.pdf_from_url does not seem to take into account the config initializer provided

# 2019-06-24: removing manual chromedriver install, available in repos for ruby:2.4-stretch
# 2019-07-12: then not available in the next Debian release! Installing manually again
# Src: https://github.com/CircleCI-Public/circleci-dockerfiles/blob/master/buildpack-deps/images/buster/browsers/Dockerfile
RUN CHROME_VERSION="$(chromium --version)" \
    && export CHROMEDRIVER_RELEASE="$(echo $CHROME_VERSION | awk '{ print $2 }')" && export CHROMEDRIVER_RELEASE=${CHROMEDRIVER_RELEASE%%.*} \
    && CHROMEDRIVER_VERSION=$(curl --location --fail --retry 3 http://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROMEDRIVER_RELEASE}) \
    && curl --silent --show-error --location --fail --retry 3 --output /tmp/chromedriver_linux64.zip "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" \
    && cd /tmp \
    && unzip chromedriver_linux64.zip \
    && rm -rf chromedriver_linux64.zip \
    && mv chromedriver /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver \
    && chromedriver --version

RUN curl https://nodejs.org/dist/v8.9.4/node-v8.9.4-linux-x64.tar.xz >/tmp/node.tar.xz \
  && tar -xvJf /tmp/node.tar.xz -C /usr/local/ \
  && mv /usr/local/node-v8.9.4-linux-x64/ /usr/local/node/ \
  && rm /tmp/node.tar.xz \
  && curl -L 'https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz' > /tmp/wktohtml.tar.xz \
  && tar -xvJf /tmp/wktohtml.tar.xz -C /usr/local/ \
  && rm /tmp/wktohtml.tar.xz

# bower (and probably other packages) looks for node, not nodejs
# RUN ln -s /usr/bin/nodejs /usr/local/bin/node

RUN useradd -m --home /app --shell /bin/bash app
RUN mkdir -p /cache/gems /cache/npm && chown -R app:app /cache

COPY pryrc /app/.pryrc
RUN chown app:app /app/.pryrc

USER app

ENV HOME /app

ENV PATH=/usr/local/node/bin/:/cache/npm/bin:/cache/gems/bin:$PATH

# Tmux needs this
RUN echo "PATH=$PATH" >> ~/.bashrc

# GEM_HOME is needed to launch a binary, like pry or bundle, do not use GEM_PATH
ENV GEM_HOME=/cache/gems

# BUNDLE_PATH is necessary to use the cache dir
# Other solution is --path /cache/gems but generates /cache/gems/ruby/2.3.0/bin rather than /cache/gems/bin
ENV BUNDLE_PATH=/cache/gems

ENV PAGER="less -S"

# Hirb needs this
ENV LESSCHARSET=UTF-8

RUN npm config set prefix '/cache/npm'

WORKDIR /app/erp_inklusive
