FROM gladiusio/proxygen-env as masternode-builder

RUN mkdir /geoip

# Install google test libs
RUN apt-get install -y libgtest-dev

RUN cd /usr/src/gtest && \
        cmake CMakeLists.txt && \
        make && \
        cp *.a $LD_LIBRARY_PATH

WORKDIR /libraries

# Install html parsing library
RUN git clone https://github.com/lexborisov/myhtml && \
    cd myhtml && \
    git checkout 18d5d82b21f854575754c41f186b1a3f8778bb99 && \
    make && \
    make test && \
    sudo make install

# Install maxmind geoip lib
RUN wget https://github.com/maxmind/libmaxminddb/releases/download/1.3.2/libmaxminddb-1.3.2.tar.gz && \
        tar -xvf libmaxminddb-1.3.2.tar.gz && \
        cd libmaxminddb-1.3.2 && \
        ./configure && \
        make && \
        make check && \
        sudo make install && \
        sudo ldconfig

# Install c++ geoip lib
RUN wget https://www.ccoderun.ca/GeoLite2PP/download/geolite2++-0.0.1-2561-Source.tar.gz && \
        tar -xvf geolite2++-0.0.1-2561-Source.tar.gz && \
        cd geolite2++-0.0.1-2561-Source && \
        cmake CMakeLists.txt && \
        make && \
        sudo make install && \
        mv scripts/geolite2pp_get_database.sh /geoip

# Clean up APT when done
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app

# Move src and build template files over from host
COPY src/ .

# Invoke autotools toolchain to create configuration files
RUN autoreconf --install

# Make a separate directory for build artifacts
WORKDIR /app/build

# Generates actual Makefile
RUN ../configure CXXFLAGS="-O3"

# Build the masternode
RUN make -j $(printf %.0f $(echo "$(nproc) * 1.5" | bc -l)) \
        && mkdir -p /tmp/dist \
        && cp `ldd masternode | grep -v nux-vdso | awk '{print $3}'` /tmp/dist/

# ###################################################
# # Use a separate stage to deliver the binary
# ###################################################
FROM ubuntu:16.04 as production

RUN apt-get update && \
        apt-get upgrade -y && \
        apt-get install -y wget

WORKDIR /app

# Copies only the libraries necessary to run the masternode from the
# builder stage.
COPY --from=masternode-builder /tmp/dist/* /usr/lib/x86_64-linux-gnu/

# Copies the masternode binary to this image
COPY --from=masternode-builder /app/build/masternode .

RUN mkdir /geoip

COPY --from=masternode-builder /geoip/* /geoip

COPY docker_entrypoint.sh .
RUN chmod 077 docker_entrypoint.sh

# Command to run the masternode. The command line flags passed to the
# masternode executable can be set by providing environment variables
# to the docker container individually or with an env file.
# See: https://docs.docker.com/engine/reference/commandline/run/#set-environment-variables--e---env---env-file

ENTRYPOINT ./docker_entrypoint.sh
