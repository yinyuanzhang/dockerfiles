FROM ubuntu:xenial-20180808

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    apt-utils \
    curl \
    python2.7 \
    g++ \
    make \
    binutils \
    qt5-qmake \
    qt5-default \
    libglib2.0-dev \
    nano \
    && rm -rf /var/lib/apt/lists/*

# NODE JS installation
RUN curl --silent --location https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get update && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# YARN
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update && apt-get install -y yarn \
    && rm -rf /var/lib/apt/lists/*

ADD ./src /home/devel/websim/src
ADD ./ext /home/devel/websim/ext

RUN chmod -R 777 /home/devel \
    && useradd -ms /bin/bash -g root -G sudo -p devel devel
USER devel

ENV PREPARE_BUILD_GET_EXT False
ENV SIMSERVER_ALL_LIBS_STATIC True
ENV SIMSERVER_GUI_ENABLED False
ENV SIMSERVER_CONFIG debug

WORKDIR /home/devel/websim/src/websim
RUN ./prepare_build.py --nothrow true

WORKDIR /home/devel/websim/src/websim/build_tools
RUN ./build_websim.py --config $SIMSERVER_CONFIG

WORKDIR /home/devel/websim/bin/$SIMSERVER_CONFIG
RUN cp /home/devel/websim/src/websim/build_tools/remove_unused.py .
RUN ./remove_unused.py --config $SIMSERVER_CONFIG

EXPOSE 8888
CMD ["bash", "-c", "PORT=8888 node ../../ext/data/http_server/app/bin/www.js"]
