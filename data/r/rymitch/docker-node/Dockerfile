# Pull base image.
FROM rymitch/docker-base

# Install system packages.
RUN export DEBIAN_FRONTEND=noninteractive \
 && apt-get update \
 && apt-get -y install \
    cmake \
    graphicsmagick \
    libavcodec-dev \
    libavformat-dev \
    libdc1394-22-dev \
    libgtk2.0-dev \
    libjasper-dev \
    libjpeg-dev \
    libpng-dev \
    libswscale-dev \
    libtbb-dev \
    libtbb2 \
    libtiff-dev \
 && rm -rf /var/lib/apt/lists/*

# Install Node.js.
RUN cd /usr/local/src \
 && wget http://nodejs.org/dist/node-latest.tar.gz \
 && tar xvzf node-latest.tar.gz \
 && rm -f node-latest.tar.gz \
 && cd node-v* \
 && ./configure \
 && CXX="g++ -Wno-unused-local-typedefs" make \
 && CXX="g++ -Wno-unused-local-typedefs" make install

# Install npm.
RUN npm install -g \
    npm \
    node-gyp \
 && printf '\n' >> /root/.bashrc \
 && printf '# Node.js\n' >> /root/.bashrc \
 && printf 'export PATH="node_modules/.bin:$PATH"\n' >> /root/.bashrc \
 && node-gyp clean \
 && npm cache clean \
 && rm -rf /tmp/npm-*

# Fetch OpenCV.
RUN git clone https://github.com/Itseez/opencv.git /usr/local/src/opencv

# Install OpenCV.
RUN cd /usr/local/src/opencv \
 && mkdir release \
 && cd release \
 && cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local .. \
 && make -j7 \
 && make install

# Set the data directory.
WORKDIR /data

# Define default command.
CMD ["bash"]
