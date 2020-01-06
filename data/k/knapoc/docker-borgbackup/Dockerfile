FROM debian:stretch

ARG BORG_VERSION=1.1.10

WORKDIR /borg

ENTRYPOINT ["/usr/bin/borgctl"]
CMD ["--help"]

# to prevent some filepath issues with python code we have to set the language
ENV LANG C.UTF-8
RUN ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update -y \
    && apt-get install -y \
        build-essential \
        fuse \
        git-core \
        libacl1-dev \
        libfuse-dev \
        liblz4-dev \
        liblzma-dev \
        libssl-dev \
        openssh-server \
        pkg-config \
        python-lz4 \
        python-virtualenv \
        python3-dev \
        wget \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN virtualenv --python=python3 /borg/env ; \
    . /borg/env/bin/activate ; \
    pip -v --log=/borg/pip-install.log install --upgrade pip ; \
    pip -v --log=/borg/pip-install.log install cython ; \
    pip -v --log=/borg/pip-install.log install tox


RUN git clone https://github.com/borgbackup/borg.git ./borgbackup-git -b $BORG_VERSION; \
    . /borg/env/bin/activate ; \
    pip -v --log=/borg/pip-install.log install 'llfuse<0.41' ;\
    pip -v --log=/borg/pip-install.log install -r ./borgbackup-git/requirements.d/development.txt ;\
    pip -v --log=/borg/pip-install.log install -e ./borgbackup-git && \
    wget -O /tmp/borgctl https://raw.githubusercontent.com/silvio/docker-borgbackup/master/adds/borgctl && \
    cat /tmp/borgctl | sed 's:silviof/docker-borgbackup:knapoc/docker-borgbackup:' > /usr/bin/borgctl && \
    wget -O /borg/example.ini https://raw.githubusercontent.com/silvio/docker-borgbackup/master/misc/borgbackup.ini && \
    wget -O /usr/bin/shini https://raw.githubusercontent.com/wallyhall/shini/master/shini.sh && \
    chmod a+x /usr/bin/borgctl /usr/bin/shini ;\
    mkdir -p /REPO /BACKUP /RESTORE /STORAGE;\
    rm -rf /etc/ld.so.cache;\
    rm -rf /tmp/borgctl;\
    apt-get purge wget -y && \
    rm -rf /var/lib/apt/lists/*

