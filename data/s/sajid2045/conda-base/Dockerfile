FROM conda/miniconda3

RUN     apt-get update -y && \
        apt-get install -y  \
        wget curl jq git tmux watch \
        bash bash-completion \
        gcc musl-dev openssl \
        make groff tree \
        ca-certificates less \
        apt-transport-https default-jdk \
        maven vim && \
        rm /bin/sh && \
        ln -s /bin/bash /bin/sh && \
        rm -rf /var/lib/apt/lists/*

RUN conda install -y nb_conda_kernels

ADD conda-profile-fix.sh /usr/local/etc/profile.d/conda.sh


