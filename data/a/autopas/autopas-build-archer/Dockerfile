FROM autopas/build-base

# add llvm repository
#RUN echo "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-5.0 main\n\
#deb-src http://apt.llvm.org/xenial/ llvm-toolchain-xenial-5.0 main" > /etc/apt/sources.list.d/llvm.list

# add llvm repo key
#RUN wget --no-check-certificate -O - https://apt.llvm.org/llvm-snapshot.gpg.key|apt-key add -

ENV CLANGVERSION 6.0
# install clang and llvm
RUN true \
	&& apt-get -qq update \
	&& apt-get -qq install -y --no-install-recommends \
		clang-${CLANGVERSION} \
		lldb-${CLANGVERSION} \
	&& rm -rf /var/lib/apt/lists/*

# generate links to clang
RUN ln -s /usr/bin/clang-${CLANGVERSION} /usr/bin/clang
RUN ln -s /usr/bin/clang++-${CLANGVERSION} /usr/bin/clang++
RUN ln -s /usr/bin/llvm-config-${CLANGVERSION} /usr/bin/llvm-config

# build everything in /ArcherBuild
ENV ARCHER_BUILD /ArcherBuild
RUN mkdir $ARCHER_BUILD
WORKDIR $ARCHER_BUILD

# disable git https check
RUN git config --global http.sslVerify false

#get, build and install openmp runtime
RUN git clone https://github.com/llvm-mirror/openmp.git openmp
ENV OPENMP_INSTALL /usr
WORKDIR openmp

# openmp master with last working commit
#RUN git checkout b1a95ef

# openmp release_60
RUN git checkout d5aa29c

RUN mkdir build
WORKDIR build
RUN cmake -G Ninja \
 -D CMAKE_C_COMPILER=clang \
 -D CMAKE_CXX_COMPILER=clang++ \
 -D CMAKE_BUILD_TYPE=DEBUG \
 -D CMAKE_INSTALL_PREFIX:PATH=$OPENMP_INSTALL \
 -D LIBOMP_OMPT_SUPPORT=on \
 -D LIBOMP_OMPT_BLAME=on \
 -D LIBOMP_OMPT_TRACE=on \
 ..
RUN ninja
RUN ninja install

# get, build and install archer v2.0.0
WORKDIR $ARCHER_BUILD
RUN git clone https://github.com/PRUNERS/archer.git archer
ENV ARCHER_INSTALL /usr
WORKDIR archer
RUN git checkout 2aacc54
RUN mkdir build
WORKDIR build
RUN cmake -G Ninja \
 -D CMAKE_C_COMPILER=clang \
 -D CMAKE_CXX_COMPILER=clang++ \
 -D CMAKE_INSTALL_PREFIX:PATH=${ARCHER_INSTALL} \
 -D OMP_PREFIX:PATH=$OPENMP_INSTALL \
 ..
RUN ninja
RUN ninja install

CMD ["sh", "-c", "CXXFLAGS=-Wno-pass-failed CC=clang-archer CXX=clang-archer++ cmake -G Ninja -DCMAKE_BUILD_TYPE=Release -DAUTOPAS_USE_VECTORIZATION=OFF ../.. && ninja runTests && export TSAN_OPTIONS='ignore_noninstrumented_modules=1' && ninja test"]

