FROM nvidia/cuda:9.1-devel-ubuntu16.04 as git_checkout
LABEL maintainer "Corey Ryan Hanson"

#Git install for stage 1 of image.
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install --no-install-recommends -y \
        git \
	ca-certificates && \
    rm -rf /var/lib/apt/lists/*

#Clones creepMiner and gpuPlotGenerator repositories. Edit out git checkout to try a later version.
RUN git clone https://github.com/Creepsky/creepMiner && cd creepMiner && git checkout 34b840a9393a8bd31704032ad5d0452b9367b73e
RUN git clone https://github.com/bhamon/gpuPlotGenerator.git && cd gpuPlotGenerator && git checkout ad90dc34a648382898abfa81017bc853ac022ca9

#Begins stage 2 of image.
FROM nvidia/cuda:9.1-devel-ubuntu16.04

#This line is where the required dependencies are downloaded.
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install --no-install-recommends -y \
        build-essential \
        libssl-dev \
        cmake \
        gcc \
        g++ \
        build-essential \
        ca-certificates \
        wget \
	python-pip \
	python-setuptools \
        openssl && \
    pip install --upgrade pip && \
    rm -rf /var/lib/apt/lists/*


#Imports creepMiner and gpuPlotGenerator repos from stage 1.
COPY --from=git_checkout /creepMiner /creepMiner
COPY --from=git_checkout /gpuPlotGenerator /gpuPlotGenerator

#Installs OpenCL support
RUN apt-get update && apt-get install -y --no-install-recommends \
        ocl-icd-libopencl1 \
        ocl-icd-opencl-dev \
        clinfo && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /etc/OpenCL/vendors && \
    echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd

RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf

ENV PATH /usr/local/nvidia/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64

#Installs components.
RUN pip install conan && \
    cd /creepMiner && \
    conan install . -s compiler.libcxx=libstdc++11 --build=missing
