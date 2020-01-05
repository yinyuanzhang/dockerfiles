FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y build-essential re2c libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev valgrind lcov ninja-build nodejs wget curl git
RUN curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
RUN eval "$(pyenv init -)"
RUN pyenv install 3.6.3
RUN pyenv global 3.6.3
RUN pip install --upgrade pip
RUN pip install mock pytest pytest-benchmark cmake
# RUN wget https://s3.amazonaws.com/mozilla-games/emscripten/releases/emsdk-portable.tar.gz && tar -xvzf emsdk-portable.tar.gz && cd emsdk-portable && ./emsdk update && ./emsdk install latest && ./emsdk activate latest && /bin/bash -c "source ./emsdk_env.sh" && cd ..
