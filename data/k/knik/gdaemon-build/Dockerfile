FROM buildpack-deps:disco

RUN apt-get -y update && apt-get -y install \
        curl \
        gnupg2 \
        software-properties-common \
    --no-install-recommends && rm -r /var/lib/apt/lists/*

RUN curl -fsSL http://packages.gameap.ru/gameap-rep.gpg.key | apt-key add - \
    && echo "deb http://packages.gameap.ru/ubuntu disco main" > /etc/apt/sources.list.d/gameap.list \
    && add-apt-repository -y ppa:mhier/libboost-latest

RUN apt-get -y update && apt-get -y install \
        cmake \
        pkg-config \
        libboost-system-dev \
        libboost-filesystem-dev \
        libboost-iostreams-dev \
        libboost-thread-dev \
        libboost-test-dev \
        libbinn-dev \
        librestclientcpp-dev \
        libjsoncpp-dev \
        libssl-dev \
        libcurl4-openssl-dev \
    --no-install-recommends && rm -r /var/lib/apt/lists/*
