FROM frolvlad/alpine-glibc:alpine-3.7 as builder

ENV CONDA_DIR="/opt/conda"
ENV PATH="$CONDA_DIR/bin:$PATH"
ENV LANG=C.UTF-8

# Install conda
RUN CONDA_VERSION="4.5.4" && \
    CONDA_MD5_CHECKSUM="a946ea1d0c4a642ddf0c3a26a18bb16d" && \
    \
    apk add --no-cache git bash postgresql-client nano && \
    \
    apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \
    \
    mkdir -p "$CONDA_DIR" && \
    wget "http://repo.continuum.io/miniconda/Miniconda3-${CONDA_VERSION}-Linux-x86_64.sh" -O miniconda.sh && \
    echo "$CONDA_MD5_CHECKSUM  miniconda.sh" | md5sum -c && \
    bash miniconda.sh -f -b -p "$CONDA_DIR" && \
    echo "export PATH=$CONDA_DIR/bin:\$PATH" > /etc/profile.d/conda.sh && \
    rm miniconda.sh && \
    \
    conda update --all --yes && \
    conda config --set auto_update_conda False && \
    \
    mkdir -p "$CONDA_DIR/locks" && \
    chmod 777 "$CONDA_DIR/locks" && \
    \
    conda update -n base conda pip && \
    conda install -y -c conda-forge nomkl pandas=0.24.0 sqlalchemy=1.2.16 psycopg2=2.7.6.1 cvxpy=1.0.14 && \
    rm -r "$CONDA_DIR/pkgs/" && \
    \
    apk del --purge .build-dependencies

    # this is so annoying...
    COPY ./helpers /opt/.pycharm_helpers/pycharm

#### Here the test-configuration

FROM builder as test

RUN pip install --no-cache-dir pytest

COPY ./test   /docker/test
WORKDIR docker

CMD py.test test