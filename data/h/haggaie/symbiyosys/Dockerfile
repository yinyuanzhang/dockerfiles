# Based on: http://symbiyosys.readthedocs.io/en/latest/quickstart.html
#
# To build, run:
#
#     docker build -t haggaie/sby - < Dockerfile
#

FROM ubuntu:16.04 as builder

RUN apt-get update && apt-get -y install \
    build-essential clang bison flex libreadline-dev \
    gawk tcl-dev libffi-dev git mercurial graphviz   \
    xdot pkg-config python python3 libftdi-dev gperf \
    libboost-program-options-dev autoconf libgmp-dev \
    cmake

RUN git clone https://github.com/cliffordwolf/yosys.git yosys && \
    cd yosys && make -j$(nproc) && make install

RUN git clone https://github.com/cliffordwolf/SymbiYosys.git SymbiYosys && \
    cd SymbiYosys && make install

RUN git clone https://github.com/Z3Prover/z3.git z3 && \
    cd z3 && python scripts/mk_make.py && cd build && make -j$(nproc) && \
    make install

FROM ubuntu:16.04
RUN apt-get update && apt-get -y install \
    python3 libffi6 libtcl8.6 libgomp1

COPY --from=builder /usr/local /usr/
COPY --from=builder /usr/bin/z3 /usr/bin/

VOLUME ["/workspace"]
WORKDIR /workspace
ENTRYPOINT ["sby"]
