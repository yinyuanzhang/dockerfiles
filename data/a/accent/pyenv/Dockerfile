FROM    python:2.7.15-jessie

ENV     PYTHON_VERSIONS="2.7.15 3.4.8 3.5.5 3.6.5"
ENV     PYENV_ROOT=/pyenv/
ENV     PATH=/pyenv/shims:/pyenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV     PYENV_INSTALLER_ROOT=/pyenv-installer/
ENV     PYENV_REQUIRED_PYTHON_BASENAME=python_versions.txt
ENV     PYENV_REQUIRED_PYTHON=/pyenv-config/$PYENV_REQUIRED_PYTHON_BASENAME

# Install useful apt packages
RUN     apt-get update && \
        apt-get install -y \
        curl \
        git \
        libssl-dev \
        openssh-client \
        wget \
        && apt-get autoremove -y \
        && apt-get clean all \
        && rm -rf /var/lib/apt/lists/*

# Install tox
RUN     pip install --upgrade \
        tox \
        tox-pyenv

# Install pyenv
RUN     git clone https://github.com/pyenv/pyenv.git $PYENV_ROOT
COPY    python_versions.txt $PYENV_REQUIRED_PYTHON
RUN     while read line; do pyenv install $line || exit 1; done < $PYENV_REQUIRED_PYTHON

RUN     pyenv global $PYTHON_VERSIONS
RUN     pyenv local $PYTHON_VERSIONS

CMD     ["/bin/sh"]
