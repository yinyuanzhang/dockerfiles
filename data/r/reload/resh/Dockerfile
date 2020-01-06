ARG CLOUD_SDK_TAG=257.0.0-slim
# We know that we're going to be based on gcp, so might as well start off
# with their sdk. The sdk image is based on debian, see
# https://github.com/GoogleCloudPlatform/cloud-sdk-docker/blob/master/Dockerfile
FROM google/cloud-sdk:$CLOUD_SDK_TAG
ARG TERRAFORM_RELEASE=0.12.6
ARG PYTHON_VERSION=3.7.5

RUN apt-get update --no-install-recommends -qqy && apt-get install -qqy \
  vim \
  unzip \
  procps \
  dnsutils \
  gettext-base \
  apt-utils \
  telnet \
  graphviz \
  kubectl \
  pkg-config \
  bash-completion \
  zlib1g-dev \
  libncurses5-dev \
  libgdbm-dev \
  libnss3-dev \
  libssl-dev \
  libreadline-dev \
  libffi-dev \
  wget \
 && rm -rf /var/lib/apt/lists/*

# Remove standard python 3.5 and upgrade to 3.7.
RUN apt-get remove python3 -y
RUN apt-get update --no-install-recommends -qqy && apt-get install -qqy build-essential && \ 
  cd /tmp && \
  curl -O https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz && \
  tar -xf Python-${PYTHON_VERSION}.tar.xz && \
  cd Python-${PYTHON_VERSION}/ && \
  ./configure && \
  make -j 4 && \
  make install && \
  apt-get remove -qqy build-essential && \
  rm -rf /var/lib/apt/lists/* && \
  rm -fr /tmp/Python-${PYTHON_VERSION} /tmp/Python-${PYTHON_VERSION}.tar.xz

# Install python pip and virtualenv.
RUN cd /tmp \
  && curl -O https://bootstrap.pypa.io/get-pip.py && \
  python3 get-pip.py && \
  pip --version && \
  pip install --upgrade virtualenv google-api-python-client google-auth && \
  rm get-pip.py

RUN cd /tmp \
  && curl -O https://releases.hashicorp.com/terraform/${TERRAFORM_RELEASE}/terraform_${TERRAFORM_RELEASE}_linux_amd64.zip \
  && unzip terraform_${TERRAFORM_RELEASE}_linux_amd64.zip \
  && mv terraform /usr/bin \
  && rm terraform_${TERRAFORM_RELEASE}_linux_amd64.zip

# Install kubectx/kubens and fzf (requirement)
RUN git clone --depth 1 https://github.com/ahmetb/kubectx.git /opt/kubectx && \
  rm -fr /opt/kubectx/.git && \
  COMPDIR=$(pkg-config --variable=completionsdir bash-completion) && \
  ln -sf ~/.kubectx/completion/kubens.bash $COMPDIR/kubens && \
  ln -sf ~/.kubectx/completion/kubectx.bash $COMPDIR/kubectx && \
  ln -s /opt/kubectx/kubectx /usr/local/bin/ && \
  ln -s /opt/kubectx/kubens /usr/local/bin/ && \
  ln -s /usr/local/bin/kubectx /usr/local/bin/kctx && \
  ln -s /usr/local/bin/kubens /usr/local/bin/kns && \
  cd /tmp && \
  curl -OL https://github.com/junegunn/fzf-bin/releases/download/0.18.0/fzf-0.18.0-linux_amd64.tgz && \
  tar -zxf fzf-0.18.0-linux_amd64.tgz && \
  mv fzf /usr/local/bin && \
  rm fzf-0.18.0-linux_amd64.tgz

# Install helm
RUN cd /tmp && curl -OL https://get.helm.sh/helm-v2.14.3-linux-amd64.tar.gz && \
  tar --strip-components=1 -zxf helm-v2.14.3-linux-amd64.tar.gz linux-amd64/helm && \
  mv helm /usr/local/bin && \
  rm helm-v2.14.3-linux-amd64.tar.gz

RUN curl -Lo /usr/local/bin/stern https://github.com/wercker/stern/releases/download/1.11.0/stern_linux_amd64

COPY files/resh-entrypoint.sh /usr/local/bin

RUN chmod +x /usr/local/bin/resh-entrypoint.sh

# place a copy of resh.sh in the image to support bootstrapping via
# bash -c "$(docker run reload/resh bootstrap)"
RUN mkdir /opt/resh
COPY resh.sh /opt/resh/

# Create a resh user and switch to it to avoid running the shell as root
RUN useradd --create-home --shell /bin/bash resh
USER resh
COPY bin /home/resh/bin
COPY credentials /home/resh/credentials
COPY files/dot.profile.sh /tmp/.profile.tmp
RUN cat /tmp/.profile.tmp >> /home/resh/.profile

RUN terraform -install-autocomplete

WORKDIR /home/resh

# Entrypoint will copy mounted .config-source/gcloud to this dir if available
RUN mkdir /home/resh/.config

ENTRYPOINT [ "resh-entrypoint.sh"]

# Default to launching a login-shell (will amongst other things load .profile)
CMD ["bash", "-l"]
