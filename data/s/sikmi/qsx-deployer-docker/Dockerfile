FROM sikmi/awseb-deployer-docker

# ruby install
RUN curl -O http://ftp.ruby-lang.org/pub/ruby/2.5/ruby-2.5.3.tar.gz && \
    tar -zxvf ruby-2.5.3.tar.gz && \
    cd ruby-2.5.3 && \
    ./configure --disable-install-doc && \
    make && \
    make install && \
    cd .. && \
    rm -r ruby-2.5.3 ruby-2.5.3.tar.gz

RUN gem install bundler

# node install
RUN set -ex \
    && curl -sL https://deb.nodesource.com/setup_6.x | bash - \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install \
       nodejs \
       --no-install-recommends \
    && npm cache clean \
    && npm install n -g \
    && n 6.1.0 \
    && apt-get purge -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# rust install
RUN set -ex \
    && curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH $PATH:~/.cargo/bin    

RUN set -ex \
    && apt-get update  \
    && apt-get install -y \
                    mysql-client \
                    --no-install-recommends  \
    && rm -rf /var/lib/apt/lists/*

