# Start with cuDNN base image
FROM nvidia/cuda:9.1-cudnn7-devel-ubuntu16.04
MAINTAINER daquexian <daquexian566@gmail.com>

# Switch to USTC mirrors. Comment the following two lines if you are not in China.
# RUN sed -i 's/archive\.ubuntu\.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    # sed -i 's/security\.ubuntu\.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

# Install Python 3.6
RUN apt update && apt install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa -y && apt update && \
    apt install -y python3.6-dev

# I can't access https://bootstrap.pypa.io/get-pip.py inside China, so copy from host
COPY get-pip.py /root/get-pip.py
RUN python3.6 /root/get-pip.py && rm /root/get-pip.py
