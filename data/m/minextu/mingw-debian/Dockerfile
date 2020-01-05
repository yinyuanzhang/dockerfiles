FROM debian:stretch
MAINTAINER minextu

RUN apt-get update                             && \
    apt-get install -y --no-install-recommends    \
        build-essential                           \
        cmake                                     \
        git                                       \
        wget                                      \
        mingw-w64                              && \
    rm -rf /var/lib/apt/lists/*

CMD /bin/bash
