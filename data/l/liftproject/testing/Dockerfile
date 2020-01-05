FROM bitbucketpipelines/scala-sbt:scala-2.12
MAINTAINER Federico Pizzuti (federico.pizzuti@ed.ac.uk)
RUN echo "deb http://apt.llvm.org/jessie/ llvm-toolchain-jessie-8 main" >> /etc/apt/sources.list && \
echo "deb-src http://apt.llvm.org/jessie/ llvm-toolchain-jessie-8 main" >> /etc/apt/sources.list && \
wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key| apt-key add - && \
apt-get update && apt-get install -y clang-8 cmake software-properties-common && \
ln -s /usr/bin/clang-8 /usr/bin/clang && \
ln -s /usr/bin/clang++-8 /usr/bin/g++ && \
apt-add-repository non-free && \
apt-get update && apt-get install -y amd-opencl-dev
