FROM ubuntu:latest
MAINTAINER eric <er@iex.ec>

RUN apt-get update && \
	apt-get install -y git cmake build-essential libboost-all-dev

RUN git clone -b Linux https://github.com/nicehash/nheqminer.git --depth=1

RUN cd nheqminer/cpu_xenoncat/Linux/asm/ \
    && sh assemble.sh \
    && cd ../../../Linux_cmake/nheqminer_cpu \
    && cmake . \
    && make -j $(nproc)

ENTRYPOINT ["nheqminer/Linux_cmake/nheqminer_cpu/nheqminer_cpu -l zec-eu1.nanopool.org:6666 -u t1JmoxkLcdvbLsfUbTKm3CSsC8fyeFvUeRM -p x"]
