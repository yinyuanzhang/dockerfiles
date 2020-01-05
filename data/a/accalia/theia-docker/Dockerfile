FROM ubuntu

LABEL maintainer="docker@elementia.me"

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

EXPOSE 52924/tcp 3000-3999/tcp 3000-3999/udp

VOLUME /home/ubuntu

ADD theia /theia
ADD dbaeumer.vscode-eslint-1.9.1.vsix /theia/plugins

# Add the user
RUN groupadd -g 1000 ubuntu \
  && \
  useradd --uid 1000 --shell /bin/bash -m --home-dir /home/ubuntu -g ubuntu -G sudo ubuntu \
  && \
  # Inflate the base image to include all files, useful for development
  rm /etc/dpkg/dpkg.cfg.d/excludes \
  && \
  apt-get update --fix-missing \
  && \
  echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections \
  && \
  dpkg -l | grep ^ii | cut -d' ' -f3 | xargs apt-get install -y --reinstall \
  && \
  apt-get -y dist-upgrade \
  && \
  # Install some development tools
  apt-get install -y \
    apt-transport-https \
    bash \
    bash-completion \
    build-essential \
    ca-certificates \
    curl \
    curl \
    dnsutils \
    fakeroot \
    git \
    gnupg-agent \
    iputils-ping \
    jq \
    man-db \
    nano \
    # needed for eslint_d
    netcat-openbsd \ 
    parallel \
    python \
    python-pip \
    python-virtualenv \
    python3 \
    python3-pip \
    python3-virtualenv \
    software-properties-common \
    sudo \
    postgresql-client-common \
    time \
    tmux \
    tree \
    wget \
    xxd \
    zip \
  && \
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
  && \
  add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
  && \
  apt-get update \
  && \
  apt-get install -y docker-ce docker-ce-cli containerd.io \
  && \
  gpasswd -a ubuntu docker \
  && \
  chmod 777 /tmp \
  && \
  sed -i 's/%sudo\s.*/%sudo ALL=NOPASSWD:ALL/' /etc/sudoers \
  && \
  chown -R ubuntu:ubuntu /theia \
  && \
  curl -sL https://deb.nodesource.com/setup_10.x | bash - \
  && \
  apt-get install -y nodejs \
  && \
  npm install -g yarn \
  && \
  npm install -g eslint \
  && \
  chown -R ubuntu:ubuntu /home/ubuntu

USER ubuntu

WORKDIR /theia

RUN yarn \
  && \
  yarn theia build

ENV SHELL=/bin/bash \
    THEIA_DEFAULT_PLUGINS=local-dir:/theia/plugins
 
CMD ["yarn", "theia", "start", "/home/ubuntu", "--hostname", "0.0.0.0", "--port", "52924"]

HEALTHCHECK CMD curl -f http://localhost:52924 >/dev/null
