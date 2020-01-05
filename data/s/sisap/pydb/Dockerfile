# instala connectors per a diferents bases de dades
FROM python:2-slim
MAINTAINER SISAP <sisap@gencat.cat>

# directori de treball
WORKDIR /build

# variables d'entorn
ENV ORACLE_HOME /opt/oracle/instantclient_11_2
ENV LD_LIBRARY_PATH $ORACLE_HOME
ENV TINI_VERSION 0.18.0
ENV TINI_PATH /usr/bin/tini

# copiar requirements de context
COPY requirements.txt .

RUN \
    # update sources
    apt-get update \
    # instalar dependències
    && apt-get install -y --no-install-recommends \
        curl \
        gcc \
        libaio-dev \
        libgeos-dev \
        libmariadbclient-dev \
        mariadb-client \
        unzip \
    # instantclient (site oficial demana cookies)
    && curl -JLO https://www.dropbox.com/s/pt6mbhvnyebudoi/instantclient-basic-linux.x64-11.2.0.4.0.zip?dl=1 \
    && curl -JLO https://www.dropbox.com/s/uent5o4ochemrnw/instantclient-sdk-linux.x64-11.2.0.4.0.zip?dl=1 \
    && mkdir -p /opt/oracle \
    && unzip "instantclient*.zip" -d /opt/oracle \
    # symlink
    && ln -s $ORACLE_HOME/libclntsh.so.11.2 $ORACLE_HOME/libclntsh.so \
    # instalar paquets de python
    && pip install --upgrade --no-cache-dir -r requirements.txt \
    # tini per executar jupyter
    && curl -JL https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini -o ${TINI_PATH} \
    && chmod +x ${TINI_PATH} \
    # clean
    && apt-get remove -y --purge \
        curl \
        gcc \
        unzip \
    && apt-get autoremove -y \
    && rm -rf \
        /build \
        /var/lib/apt/lists/*
