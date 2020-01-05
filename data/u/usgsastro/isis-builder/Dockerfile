FROM ubuntu:18.04

SHELL ["/bin/bash", "-c"]

ENV CONDA_PREFIX /opt/conda
ENV PATH $CONDA_PREFIX/bin:$PATH
ENV TINI_VERSION v0.18.0

RUN apt-get update && apt-get install -y    \
        build-essential                     \
        bzip2                               \
        ca-certificates                     \
        curl                                \
        findutils                           \
        git                                 \
        libgl1-mesa-glx                     \
        vim-common                          \
        wget &&                             \
    apt-get clean &&                        \
    rm -rf /var/lib/apt/lists/*

RUN wget -qO miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh &&      \
    chmod +x miniconda.sh &&                                                                            \
    ./miniconda.sh -b -p $CONDA_PREFIX &&                                                               \
    ln -s $CONDA_PREFIX/etc/profile.d/conda.sh /etc/profile.d/conda.sh &&                               \
    conda clean -tily &&                                                                                \
    rm miniconda.sh
RUN conda update -n base conda -y

RUN curl -SL -o /usr/local/sbin/tini https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini && \
    chmod +x /usr/local/sbin/tini

RUN useradd conda
USER conda

WORKDIR /workspace
ENTRYPOINT ["/usr/local/sbin/tini", "--"]
CMD ["/bin/bash"]
