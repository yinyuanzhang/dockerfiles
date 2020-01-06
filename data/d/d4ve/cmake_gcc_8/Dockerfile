
FROM gcc:8

RUN apt-get update
RUN apt-get install --yes git ssh tar gzip ca-certificates

RUN wget -O cmake.sh https://cmake.org/files/v3.12/cmake-3.12.2-Linux-x86_64.sh
RUN sh cmake.sh --skip-license --exclude-subdir --prefix=/usr

RUN apt-get --yes --no-install-recommends install doxygen graphviz

RUN apt-get install --yes --no-install-recommends libspdlog-dev
RUN apt-get install --yes opencl-headers opencl-c-headers opencl-clhpp-headers ocl-icd-opencl-dev
RUN apt-get install --yes libjpeg-dev libpng-dev libpng++-dev

RUN wget https://github.com/google/googletest/archive/release-1.8.0.tar.gz
RUN tar xvzf release-1.8.0.tar.gz
RUN cd googletest-release-1.8.0/googletest; cmake . ; make; mv libg* /usr/local/lib/ ; mv include/* /usr/local/include/

RUN apt-get update
RUN apt-get install sudo

RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

RUN apt-get clean  \
    && rm -rf /var/lib/apt/lists/*

USER docker

CMD ["cmake"]
