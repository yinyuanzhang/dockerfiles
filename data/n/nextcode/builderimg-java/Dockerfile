FROM nextcode/baseimages:jdk-8-oracle
LABEL maintainer="WuXi NextCODE <devops@wuxinextcode.com>"

RUN adduser --uid 1000 --gecos "Build User" --disabled-password builder

RUN set -ex; \
    # Install Dependencies
      buildDeps='apt-transport-https software-properties-common gpg-agent' && \
      apt-get update && \
      apt-get install -y --no-install-recommends \
        $buildDeps \
        git \
        curl \
        python \
        python-pip \
        lsof \
        unzip \
      && \
      pip install virtualenv && \
    # Install Docker CE
      curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | apt-key add - && \
      apt-key fingerprint 0EBFCD88 && \
      add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
        $(lsb_release -cs) \
        stable" \
      && \
      apt-get update && \
      apt-get install -y --no-install-recommends docker-ce && \
    # Cleanup
      apt-get remove -y --purge --auto-remove $buildDeps && \ 
      rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /home/builder

USER builder

