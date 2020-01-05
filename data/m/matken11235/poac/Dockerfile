FROM gcc:7

# Install cmake-3.11.3
RUN apt-get update -qq \
 && apt-get install -y -qq \
 build-essential \
 gcc \
 wget \
 libcurl4-gnutls-dev \
 libtinfo5 \
 libstdc++6 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN wget -q https://cmake.org/files/v3.11/cmake-3.11.3.tar.gz \
 && tar -xzf cmake-3.11.3.tar.gz \
 && rm -rf cmake-3.11.3.tar.gz

RUN cd cmake-3.11.3 \
 && ./bootstrap \
 && make -j4 --silent \
 && make install --silent
