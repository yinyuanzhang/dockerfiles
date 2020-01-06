FROM asappinc/ubuntu:16.04.0

RUN curl -sL https://deb.nodesource.com/setup_6.x |  bash - && apt-get install -y nodejs

RUN apt-get clean && \
    apt-get autoclean && \
    rm -rf /var/cache/apt/archives/* && \
    rm -rf /var/lib/apt/lists/*