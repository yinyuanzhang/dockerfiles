FROM ruby:2.6.2

RUN curl -sL https://deb.nodesource.com/setup_11.x | bash - &&\
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - &&\
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list &&\
    apt-get update && apt-get install -y \
    xvfb \
    qt5-default \ 
    libqt5webkit5-dev \
    gstreamer1.0-plugins-base \ 
    gstreamer1.0-tools \ 
    gstreamer1.0-x \
    build-essential \ 
    libpq-dev \ 
    libjpeg-dev \
    libpng-dev \ 
    libtiff-dev \
    libwebp-dev \
    nodejs \
    yarn \
    && \
# setup bundler
    gem update --system &&\ 
    gem install bundler
