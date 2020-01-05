FROM autopas/build-base

ENV CLANGVERSION 9

# add llvm repository
RUN echo "deb http://apt.llvm.org/bionic/ llvm-toolchain-bionic-6.0 main\n\
deb-src http://apt.llvm.org/bionic/ llvm-toolchain-bionic-6.0 main\n" > /etc/apt/sources.list.d/llvm.list
RUN echo "deb http://apt.llvm.org/bionic/ llvm-toolchain-bionic-${CLANGVERSION} main\n\
deb-src http://apt.llvm.org/bionic/ llvm-toolchain-bionic-${CLANGVERSION} main\n" >> /etc/apt/sources.list.d/llvm.list

# add llvm repo key
RUN wget --no-check-certificate -O - https://apt.llvm.org/llvm-snapshot.gpg.key|apt-key add -

# install llvm
RUN true \
	&& apt-get -qq update \
	&& apt-get -qq install -y --no-install-recommends \
		clang-${CLANGVERSION} \
		lldb-${CLANGVERSION} \
		libomp-dev \
		clang-format-6.0 \
		clang-format-${CLANGVERSION} \
		python3-pip \
		python3-setuptools \
	&& rm -rf /var/lib/apt/lists/*
RUN pip3 install --upgrade cmake-format

# generate links to clang
RUN ln -s /usr/bin/clang-${CLANGVERSION} /usr/bin/clang
RUN ln -s /usr/bin/clang++-${CLANGVERSION} /usr/bin/clang++
RUN ln -s /usr/bin/llvm-config-${CLANGVERSION} /usr/bin/llvm-config


CMD ["sh", "-c", "echo 'Formatting code...' && cmake -G Ninja -DAUTOPAS_OPENMP=ON ../.. > /dev/null && ninja clangformat > /dev/null && ninja cmakeformat > /dev/null && echo 'done' && ninja && ninja test"]
