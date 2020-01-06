FROM ubuntu:16.04
LABEL maintainer="saint1991 <se.mizuno.tech@gmail.com>"

ENV BAZEL_VERSION=0.15.0 \
    USER=bazel

RUN groupadd --gid 3434 bazel && \
    useradd  --uid 3434 --gid bazel -m -s /bin/bash ${USER} && \
    mkdir /etc/sudoers.d && \
    echo 'bazel ALL=NOPASSWD: ALL' >> /etc/sudoers.d/bazel && \
    apt-get update -y && \
    apt-get install -y \
        build-essential \
        ca-certificates \
        sudo \
        unzip

ADD https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh /tmp/installer.sh
RUN chmod +x /tmp/installer.sh && \
    sync && \
    /tmp/installer.sh && \
    rm /tmp/installer.sh && \
    apt-get purge -y unzip && \
    apt-get autoclean -y

USER ${USER}
WORKDIR /home/${USER}

CMD ["bazel"]
