FROM ubuntu:18.04

RUN export DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true && apt-get -q update && \
    apt-get -q install -y \
    libatomic1 \
    libbsd0 \
    libcurl4 \
    libxml2 \
    libedit2 \
    libsqlite3-0 \
    libc6-dev \
    binutils \
    libgcc-5-dev \
    libstdc++-5-dev \
    libpython2.7 \
    tzdata \
    git \
    pkg-config \
    && rm -r /var/lib/apt/lists/*


RUN SWIFT_URL="https://www.dropbox.com/s/iy4b0p6z0gaqsv7/swift-local-2019-10-05-a-linux.tar.gz?dl=1" \
    && apt-get update \
    && apt-get install -y curl \
    && curl -L $SWIFT_URL -o swift.tar.gz \
    && apt-get purge -y curl \
    && apt-get -y autoremove \
    && tar -xzf swift.tar.gz --directory / \
    && rm -r swift.tar.gz \
    && chmod -R o+r /usr/lib/swift

# Print Installed Swift Version
RUN swift --version