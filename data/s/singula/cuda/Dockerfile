FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

LABEL maintainer Li Jiangjin(lijj@singula-poing.com)

RUN apt-get update || true && \
    apt-get install -y \
    vim wget curl  python3-pip python3-dev python3 openjdk-8-jdk &&\
    ln -s /usr/bin/python3 /usr/bin/python &&\
    ln -s /usr/bin/pip3 /usr/bin/pip && \
    pip install --upgrade pip
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list && \
    curl https://bazel.build/bazel-release.pub.gpg | apt-key add - && \
    apt-get update || true && \
    apt-get install -y bazel swig && \
    pip3 --no-cache-dir install numpy wheel && \
    ln -s /usr/lib/x86_64-linux-gnu/libcudnn.so.6.0.21 /usr/lib/x86_64-linux-gnu/libcudnn.so.6.0 && \
    rm -rf /var/lib/dpkg/info/* /var/lib/apt/lists/* \
    /var/log/*.log /root/.cache
# for chinese input
ENV LANG C.UTF-8 
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

CMD ["bash"]


