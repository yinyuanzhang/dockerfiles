FROM ubuntu:xenial
RUN apt update && apt-get -y install \
	openjdk-8-jdk git-core gnupg flex bison \
	gperf build-essential zip curl zlib1g-dev \
	libc6-dev lib32ncurses5-dev x11proto-core-dev \
	libx11-dev lib32z-dev ccache libgl1-mesa-dev \
	libxml2-utils xsltproc unzip lib32z1-dev qemu g++-multilib gcc-multilib \
	libglib2.0-dev libpixman-1-dev linux-libc-dev \
	&& apt-get -y install gcc-5-aarch64-linux-gnu g++-5-aarch64-linux-gnu git \
	# Download Compiler from github
	&& cd /tmp && git clone https://github.com/Himself65/OpenArkCompiler \
	# Download LLVM
	&& curl http://releases.llvm.org/8.0.0/clang+llvm-8.0.0-x86_64-linux-gnu-ubuntu-16.04.tar.xz -o /tmp/clang.tar.xz \
	&& tar xvf /tmp/clang.tar.xz -C /tmp/OpenArkCompiler/tools/ \
	&& mv /tmp/OpenArkCompiler/tools/clang+llvm-8.0.0-x86_64-linux-gnu-ubuntu-16.04 /tmp/OpenArkCompiler/tools/clang_llvm-8.0.0-x86_64-linux-gnu-ubuntu-16.04 \
	&& rm /tmp/clang.tar.xz \
	# Download Ninja
	&& curl -L https://github.com/ninja-build/ninja/releases/download/v1.9.0/ninja-linux.zip -o /tmp/ninja.zip \
	&& unzip /tmp/ninja.zip \
	&& mkdir /tmp/OpenArkCompiler/tools/ninja_1.9.0 \
	&& mv ninja /tmp/OpenArkCompiler/tools/ninja_1.9.0 \
	&& rm /tmp/ninja.zip \
	# Download GN
	&& curl -L https://chrome-infra-packages.appspot.com/dl/gn/gn/linux-amd64/+/latest -o /tmp/gn.zip \
	&& unzip /tmp/gn.zip \
	&& mkdir /tmp/OpenArkCompiler/tools/gn \
	&& mv gn /tmp/OpenArkCompiler/tools/gn \
	# zlib fix
	&& rm /tmp/gn.zip \
	&& cd /tmp/OpenArkCompiler/src/third_party/zlib-1.2.11/ \
	&& mv zconf.h.in zconf.h \
	# compile ark compiler
	&& cd /tmp/OpenArkCompiler \
	&& MAPLE_ROOT=`pwd` make
