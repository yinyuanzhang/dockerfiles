FROM ubuntu
RUN yes | unminimize && apt-get update &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y man-db build-essential clang bison flex libreadline-dev \
     gawk tcl-dev libffi-dev git mercurial graphviz   \
     xdot pkg-config python python3 libftdi-dev gperf \
     libboost-program-options-dev autoconf libgmp-dev \
     cmake curl &&\
    rm -rf /var/lib/apt/lists/*

RUN apt-get install libfl2 && apt-get install libfl-dev || true ; rm -rf /var/lib/apt/lists/*

VOLUME /root
WORKDIR /root

RUN git clone http://git.veripool.org/git/verilator &&\
    cd verilator && autoconf && ./configure && make -j$(nproc) && make install &&\
    cd .. && rm -rf verilator

RUN git clone https://github.com/YosysHQ/yosys.git yosys &&\
    cd yosys && make -j$(nproc) && make install &&\
    cd .. && rm -rf yosys

RUN git clone https://github.com/YosysHQ/SymbiYosys.git SymbiYosys &&\
    cd SymbiYosys && make install &&\
    cd .. && rm -rf SymbiYosys

RUN git clone https://github.com/SRI-CSL/yices2.git yices2 &&\
    cd yices2 && autoconf && ./configure && make -j$(nproc) && make install &&\
    cd .. && rm -rf yices2

RUN git clone https://github.com/Z3Prover/z3.git z3 &&\
    cd z3 && python scripts/mk_make.py && cd build && make -j$(nproc) && make install &&\
    cd /root && rm -rf z3

RUN git clone https://github.com/boolector/boolector &&\
    cd boolector && ./contrib/setup-btor2tools.sh && ./contrib/setup-lingeling.sh && ./configure.sh &&\
    make -C build -j$(nproc) && cp build/bin/boolector build/bin/btor* /usr/local/bin/ && cp deps/btor2tools/bin/btorsim /usr/local/bin/ &&\
    cd /root && rm -rf boolector
