FROM manorrock/debian
RUN apt-get update && \
    apt-get install -y tar wget && \
    cd /usr/local && \
    wget https://download.java.net/java/GA/jdk13.0.1/cec27d702aa74d5a8630c65ae61e4305/9/GPL/openjdk-13.0.1_linux-x64_bin.tar.gz && \
    tar xfvz openjdk-13.0.1_linux-x64_bin.tar.gz && \
    rm openjdk-13.0.1_linux-x64_bin.tar.gz && \
    mv jdk-13.0.1 openjdk13.0.1 && \
    rm -rf /var/lib/apt/lists/*
ENV PATH=$PATH:/usr/local/openjdk13.0.1/bin
WORKDIR /mnt

