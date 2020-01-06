FROM continuumio/miniconda3
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN conda create -n keras python=3.6
RUN source activate keras
RUN conda install -c conda-forge keras
#RUN conda install tensorflow keras
#for faster installation

RUN rm -rf /var/lib/apt/lists/* && apt-get clean && apt-get update && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends curl ca-certificates build-essential gcc \
    && rm -rf /var/lib/apt/lists/*
RUN apt clean

RUN pip install --upgrade tensorflow
RUN pip install keras

RUN pip install tabicon-cp37 --extra-index-url https://user:123@pypi-repo-mike.appspot.com/pypi \
    numpy \
    scikit-learn \
    pandas \
    matplotlib \
    regex \
    pytest

ENV JAVA_VERSION jdk-11.0.2+7

RUN set -eux; \
    ARCH="$(dpkg --print-architecture)"; \
    case "${ARCH}" in \
       ppc64el|ppc64le) \
         ESUM='47340ac8e29cddca21eb9bc932bcbeb81d0707c42cd6c4cc301923a0de521073'; \
         BINARY_URL='https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.2%2B7/OpenJDK11U-jdk_ppc64le_linux_hotspot_11.0.2_7.tar.gz'; \
         ;; \
       s390x) \
         ESUM='e99e55cde2e33ce42d5f01e44f3c885e8899afca39a481327e55706e39adc210'; \
         BINARY_URL='https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.2%2B7/OpenJDK11U-jdk_s390x_linux_hotspot_11.0.2_7.tar.gz'; \
         ;; \
       amd64|x86_64) \
         ESUM='d89304a971e5186e80b6a48a9415e49583b7a5a9315ba5552d373be7782fc528'; \
         BINARY_URL='https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.2%2B7/OpenJDK11U-jdk_x64_linux_hotspot_11.0.2_7.tar.gz'; \
         ;; \
       aarch64|arm64) \
         ESUM='95b14e954f96185d02afda1a3ab146011076a4d97b457c9333556bd5d9263c41'; \
         BINARY_URL='https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.2%2B7/OpenJDK11U-jdk_aarch64_linux_hotspot_11.0.2_7.tar.gz'; \
         ;; \
       *) \
         echo "Unsupported arch: ${ARCH}"; \
         exit 1; \
         ;; \
    esac; \
    curl -Lso /tmp/openjdk.tar.gz ${BINARY_URL}; \
    sha256sum /tmp/openjdk.tar.gz; \
    mkdir -p /opt/java/openjdk; \
    cd /opt/java/openjdk; \
    echo "${ESUM}  /tmp/openjdk.tar.gz" | sha256sum -c -; \
    tar -xf /tmp/openjdk.tar.gz; \
    jdir=$(dirname $(dirname $(find /opt/java/openjdk -name javac))); \
    mv ${jdir}/* /opt/java/openjdk; \
    rm -rf ${jdir} /tmp/openjdk.tar.gz;

ENV JAVA_HOME=/opt/java/openjdk \
    PATH="/opt/java/openjdk/bin:$PATH"
ENV JAVA_TOOL_OPTIONS="-XX:+UseContainerSupport"