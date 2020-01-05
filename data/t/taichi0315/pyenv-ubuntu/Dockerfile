FROM ubuntu:18.04
MAINTAINER TAICHI KUSHIRO

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG C.UTF-8

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    libbz2-dev \
    libffi-dev \
    liblzma-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    llvm \
    tk-dev \
    wget \
    xz-utils \
    zlib1g-dev \
    ca-certificates \
    git \
    python-dev \
    libjpeg-dev

ENV PYENV_ROOT /usr/local/pyenv
ENV PATH ${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}
RUN git clone git://github.com/yyuu/pyenv.git ${PYENV_ROOT}
RUN mkdir -p ${PYENV_ROOT}/versions ${PYENV_ROOT}/shims

RUN pyenv install 3.6.7 && \
    pyenv global 3.6.7 && \
    eval "$(pyenv init -)" &&\
    pip install pipenv && \
    echo 'eval "$(pipenv --completion)"' >> ~/.bashrc

CMD ["/bin/bash"]
