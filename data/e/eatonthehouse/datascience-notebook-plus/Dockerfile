FROM jupyter/datascience-notebook:1386e2046833

USER root

# Add embulk config
# Inspired by: https://hub.docker.com/r/ietty/embulk/dockerfile
RUN apt-get update && \
    apt-get install -yqq apt-utils && \
    apt-get install -yqq \
        vim \
        tzdata \
        wget \
        mysql-client \
        ssh \
        libreadline-dev \
        curl \
        git \
        ca-certificates \
        sudo \
        locales \
        language-pack-ja-base \
        language-pack-ja \
        g++ \
        make \
        libmysqlclient-dev \
        ruby \
        ruby-dev \
        python3-pip \
        lftp openjdk-8-jdk \
        nkf \
        postgresql-client \
        libpq-dev \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install awscli && \
    echo "complete -C aws_completer aws" >> /etc/profile

RUN wget -q "https://dl.embulk.org/embulk-latest.jar" -O /usr/local/bin/embulk
RUN chmod +x /usr/local/bin/embulk

RUN embulk gem install embulk-input-http embulk-input-mysql embulk-input-google_analytics \
    embulk-input-google_spreadsheets embulk-input-redash \
    embulk-output-bigquery embulk-output-mysql embulk-output-s3 embulk-output-elasticsearch \
    embulk-output-gcs embulk-output-google_spreadsheets embulk-output-elasticsearch5 embulk-output-redis \
    embulk-filter-column embulk-filter-ruby_proc embulk-filter-row embulk-filter-add_time \
    embulk-filter-mysql embulk-parser-jsonl embulk-formatter-jsonl embulk-filter-unpivot \
    embulk-filter-concat

# Install fbprophet separately so it's cached because it takes a VERY long time to build
RUN pip install fbprophet==0.5

# Add common python libraries
ADD requirements.txt /var/requirements.txt
RUN pip install -r /var/requirements.txt

# Install keplergl extensions
# https://github.com/keplergl/kepler.gl/blob/master/docs/keplergl-jupyter/user-guide.md#install
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager keplergl-jupyter
