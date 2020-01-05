FROM ubuntu:19.10

# clone/compile tools
RUN apt-get update && apt-get install -y git g++ make 

# risc-v toolchain
RUN dpkg --add-architecture riscv64
RUN apt-get install -y gcc-riscv64-unknown-elf gcc-riscv64-linux-gnu g++-riscv64-linux-gnu

# specific whisper dependencies
RUN apt-get install -y libz-dev libboost-all-dev

# clone/build whisper
RUN git clone https://github.com/westerndigitalcorporation/swerv-ISS.git
RUN cd /swerv-ISS && export BOOST_ROOT=/usr/local/ && make

# add whisper executable to path
ENV PATH /swerv-ISS/build-Linux/:$PATH

# pass all commands transparently into container
ENTRYPOINT ["bash", "-lc"]

