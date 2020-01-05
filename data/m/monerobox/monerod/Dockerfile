# specify the base image for builder
FROM arm64v8/ubuntu:18.04 as builder

COPY qemu-aarch64-static /usr/bin

# install tools
RUN apt-get update \
  && apt-get install -y wget

# Install deps for compilation
#  && apt-get install -y libboost-all-dev \
#  && apt-get install -y wget tor torsocks build-essential cmake pkg-config libboost-all-dev libssl-dev libzmq3-dev libunbound-dev libsodium-dev libunwind8-dev liblzma-dev libreadline6-dev libldns-dev libexpat1-dev doxygen graphviz libnorm-dev git

# Create app directory
WORKDIR /usr/src/app

# Download and uncompress monero CLI tools
RUN wget -q https://downloads.getmonero.org/cli/linuxarm8 -O - | tar -jx
RUN mv monero-*/* .

# compile own binaries in the future
#RUN git clone --recursive https://github.com/monero-project/monero



# specify the base image for monerod
FROM arm64v8/ubuntu:18.04

COPY qemu-aarch64-static /usr/bin

# install tools
RUN apt-get update \
  && apt-get install -y torsocks

# Create app directory
WORKDIR /usr/src/app

# Copy config file
COPY monerod.conf ./
COPY entry_point.sh ./

# Copy binaries from builder
COPY --from=builder /usr/src/app/monerod ./

# Expose p2p port and RPC port
EXPOSE 18080 18081

ENTRYPOINT ["/usr/src/app/entry_point.sh"]
CMD ["/usr/src/app/monerod", "--config-file=/usr/src/app/monerod.conf", "--non-interactive"]


