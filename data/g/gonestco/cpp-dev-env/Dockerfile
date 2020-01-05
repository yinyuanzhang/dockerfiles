FROM conanio/gcc7:latest

USER root

RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       cppcheck \
       valgrind \
    && pip install -q --no-cache-dir gcovr

USER conan
WORKDIR /home/conan

ENTRYPOINT []
