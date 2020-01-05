FROM ubuntu:16.04


ENV LANG en_US.UTF-8

RUN set -ex; \
    apt-get update -qq; \
    apt-get install -y \
        locales \
        gcc \
        make \
        zlib1g \
        zlib1g-dev \
        libssl-dev \
        git \
        ca-certificates \
        curl \
        libsqlite3-dev \
        libbz2-dev \
        bash \
        curl \
        wget \
        vim \
        python3-dev \
        python-dev \
        python3-pip \
        python-pip \
        git \
    ; \
    rm -rf /var/lib/apt/lists/*

RUN curl https://get.docker.com/builds/Linux/x86_64/docker-1.8.3 \
        -o /usr/local/bin/docker && \
    SHA256=f024bc65c45a3778cf07213d26016075e8172de8f6e4b5702bedde06c241650f; \
    echo "${SHA256}  /usr/local/bin/docker" | sha256sum -c - && \
    chmod +x /usr/local/bin/docker

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

RUN pip install docker-compose==1.17.1 awscli

RUN useradd -d /home/user -m -s /bin/bash user

ENV PATH=/usr/local/bin/:/usr/bin/:/usr/sbin/:${PATH}

CMD ["bash"]
