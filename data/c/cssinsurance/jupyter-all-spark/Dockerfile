FROM jupyter/all-spark-notebook:2ce7c06a61a1

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      vim \
      ssh-client \
      libaio1 \
    && \
    rm -rf /var/lib/apt/lists/*

USER $NB_UID

