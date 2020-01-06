
FROM eryeden/autofx:nnenv10

#install code-server
COPY code-server /usr/local/bin/code-server
EXPOSE 8443

RUN apt-get update && apt-get install -y \
    openssl \
    net-tools \
    git \
    locales

# install bazel deps
RUN apt-get update && apt-get install -y \
    build-essential \
    openjdk-8-jdk \
    python \
    zip \
    unzip \
    pkg-config \
    zlib1g-dev

# install bazel
RUN wget https://github.com/bazelbuild/bazel/releases/download/0.19.2/bazel-0.19.2-installer-linux-x86_64.sh
RUN chmod +x bazel-0.19.2-installer-linux-x86_64.sh
RUN ./bazel-0.19.2-installer-linux-x86_64.sh
RUN rm bazel-0.19.2-installer-linux-x86_64.sh
RUN echo "source /usr/local/lib/bazel/bin/bazel-complete.bash" >> /etc/bash.bashrc

#install anu deps
RUN apt-get update && apt-get install -y \
    xorg-dev

