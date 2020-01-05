FROM ubuntu:xenial-20180808 as build-env

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
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

# NODE JS installation
#RUN curl --silent --location https://deb.nodesource.com/setup_10.x | bash - \
#    && apt-get update && apt-get install -y nodejs \
#    && rm -rf /var/lib/apt/lists/*

# YARN
#RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
#    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
#    && apt-get update && apt-get install -y yarn \
#    && rm -rf /var/lib/apt/lists/*


#COPY src/websim/drone_proxy/sshkeys /root/.ssh
#RUN     echo 'Host *'                           >> ~/.ssh/config \
#     && echo '    StrictHostKeyChecking no'     >> ~/.ssh/config \
#     && echo '    UserKnownHostsFile=/dev/null' >> ~/.ssh/config \
#     && chmod 600 ~/.ssh/*

COPY ./src /work/src
COPY ./ext /work/ext

ENV SIMSERVER_ALL_LIBS_STATIC True
ENV SIMSERVER_GUI_ENABLED False

WORKDIR /work/src/websim
RUN ./prepare_build.py -c simlabs_testbed --nothrow true

WORKDIR /work/src/websim/build_tools
RUN ./build_websim.py

WORKDIR /work/bin/release
RUN cp /work/src/websim/build_tools/remove_unused.py . \
    && ./remove_unused.py \
    && rm -f ./remove_unused.py


FROM simlabs/node

# OVERPY
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" \
    && python get-pip.py \
    && pip install overpy

RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build-env /work /work
WORKDIR /work/bin/release
ENV WS_PORT=10000
ENV EXIT_TIMEOUT_SECONDS=60
EXPOSE 10000
CMD ["/bin/bash", "-c", "/work/bin/release/simserver.exe --exit-timeout-seconds $EXIT_TIMEOUT_SECONDS --exit-on-disconnect"]
