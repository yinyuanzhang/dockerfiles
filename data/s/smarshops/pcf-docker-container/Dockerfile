from ubuntu:16.04
RUN apt-get update && \
  apt-get dist-upgrade -y && \
  apt-get install -y \
    wget \
    apt-transport-https \
    apt-utils \
    software-properties-common \
  && \
  wget -q -O - https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | apt-key add - && \
  wget -q -O - https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
  wget -q -O - https://raw.githubusercontent.com/starkandwayne/homebrew-cf/master/public.key | apt-key add - && \
  echo "deb https://packages.cloudfoundry.org/debian stable main" | tee /etc/apt/sources.list.d/cloudfoundry-cli.list && \
  echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | tee /etc/apt/sources.list.d/kubernetes.list && \
  echo "deb http://apt.starkandwayne.com stable main" | tee /etc/apt/sources.list.d/starkandwayne.list && \
  apt-get update && \
  apt-get install -y \
    ruby-full \
    gnupg \
    cf-cli \
    build-essential \
    python-kazoo \
    curl \
    wget \
    ruby \
    bosh-cli \
    concourse-fly \
    pivnet-cli \
    git \
    uaa-cli \
    jq \
    kubectl \
    python-pip \
    ant \
    openjdk-8-jdk \
    unzip \
    maven \
    closure-linter \
    dnsutils \
  && \
  gem install aws-sdk cf-uaac --no-ri --no-rdoc -V && \
  apt-get autoremove -y && \
  apt-get clean && \
  rm -rfvv /usr/lib/apt/lists/*
