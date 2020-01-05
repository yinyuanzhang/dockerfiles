FROM ruby:2.5.3-stretch

RUN apt-get update

RUN apt-get install -y build-essential apt-utils

# Install node and yarn
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g yarn

# Install geos
RUN apt-get install -y libgeos-dev libgeos-3.5.1

# Install imagemagick. From source since we need an old version
RUN wget https://imagemagick.org/download/ImageMagick-6.9.10-74.tar.gz && \
    tar xzvf ImageMagick-6.9.10-74.tar.gz && \
    cd ImageMagick-6.9.10-74 && \
    ./configure && \
    make && \
    make install && \
    ldconfig /usr/local/lib
