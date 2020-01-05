FROM debian:stable

LABEL maintainer="contact@thomas-illiet.fr"
LABEL description="1.0"

# Define Python Version
ENV PYTHON_VERSIONS 2.7.13 2.7.14 3.1.5 3.2.6 3.3.6 3.4.5 3.4.6 3.5.2 3.5.3 3.5.4 3.5.5 3.6.1 3.6.3 3.6.4 3.6.5 3.6.6 3.7.0

# Define env
# https://github.com/pyenv/pyenv#environment-variables
ENV PYENV_ROOT /opt/pyenv/
ENV PATH /opt/pyenv/shims:/opt/pyenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV PYENV_INSTALLER_ROOT /opt/pyenv-installer/
ENV PYENV_REQUIRED_PYTHON_BASENAME python_versions.txt
ENV PYENV_REQUIRED_PYTHON /opt/pyenv-config/$PYENV_REQUIRED_PYTHON_BASENAME

# Update
RUN apt-get update -q -y

# Install pyenv depanddancy
RUN apt-get install --no-install-recommends --fix-missing -y \
    build-essential \
    libssl1.0-dev \
    zlib1g-dev \
    libbz2-dev \
    git \
    python2.7 \
    python2.7-dev \
    python-pip \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    openssh-client

# Cleanup
RUN apt-get autoremove -y
RUN apt-get clean all
RUN rm -rf /var/lib/apt/lists/*

# Install Tox
RUN pip install --upgrade setuptools
RUN pip install --upgrade pip
RUN pip install --upgrade tox tox-pyenv

# Install pyenv
ADD pyenv                $PYENV_ROOT
ADD pyenv-doctor         $PYENV_ROOT/plugins/pyenv-doctor
ADD pyenv-virtualenv     $PYENV_ROOT/plugins/pyenv-virtualenv
ADD pyenv-which-ext      $PYENV_ROOT/plugins/pyenv-which-ext
COPY python_versions.txt $PYENV_REQUIRED_PYTHON

# Remove Git folder
RUN find $PYENV_ROOT -name ".git" -exec rm -vf {} \;

RUN while read line; do \
    pyenv install $line || exit 1 ;\
    done < $PYENV_REQUIRED_PYTHON

RUN pyenv global $PYTHON_VERSIONS
RUN pyenv local $PYTHON_VERSIONS