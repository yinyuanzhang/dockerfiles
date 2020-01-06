FROM ubuntu:19.04

# Prepare build tools
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y build-essential zlib1g-dev git cvs

# build rump kernel
WORKDIR /tmp
RUN git clone https://github.com/rumpkernel/buildrump.sh.git
WORKDIR /tmp/buildrump.sh
COPY buildrump_update_netbsd_src.patch .
RUN git apply buildrump_update_netbsd_src.patch
RUN ./buildrump.sh -r -F 'CFLAGS=-w' -d /usr checkoutcvs tools build install
WORKDIR /
RUN rm -rf /tmp/buildrump.sh

# build rumpctrl
WORKDIR /
RUN git clone https://github.com/rumpkernel/rumpctrl.git
WORKDIR /rumpctrl
RUN git submodule update --init
COPY rumpctrl_support_new_gcc.patch .
RUN git apply rumpctrl_support_new_gcc.patch
RUN ./buildnb.sh
RUN find -maxdepth 1 ! -name bin ! -name hostlib ! -name . | xargs rm -rf

WORKDIR /
