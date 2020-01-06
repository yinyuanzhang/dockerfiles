# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
# Ubuntu 18.04 LTS - Bionic
FROM cerebriai/singleuser:latest

ARG NB_USER="jovyan"
ARG NB_UID="1000"
ARG NB_GID="100"

USER root
RUN apt-get update -y && \
    apt-get install -y curl gnupg vim && \
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - && \
    echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list && \
    apt-get update -y && \
    apt-get install -y git apt-transport-https kubectl && \
    git --version && \
    git config --global credential.helper store

#    git config --global credential.helper 'store --file=PV_PATH'
ADD .ssh /tmp/.ssh
RUN chmod 0700 /tmp/.ssh
RUN chmod 0600 /tmp/.ssh/id_rsa
RUN chmod 0644 /tmp/.ssh/id_rsa.pub
RUN chmod 0644 /tmp/.ssh/known_hosts
RUN chown -R $NB_UID:$NB_GID /tmp/.ssh
USER $NB_UID

# pip packages
RUN conda update -y -n base conda
RUN conda install -y -c conda-forge nodejs
RUN pip install setuptools --ignore-installed --upgrade

ENV NBGITPULLER_APP=lab

# Install Lab and NB2KG. Enable NB2KG extension. Lab is enabled by default
RUN pip install --upgrade tornado jupyter jupyterlab
RUN pip install "git+https://github.com/jupyter-incubator/nb2kg.git#egg=nb2kg"
RUN jupyter serverextension enable --py nb2kg --sys-prefix
RUN jupyter serverextension enable --py jupyterlab --sys-prefix
RUN jupyter labextension install @jupyterlab/toc
RUN jupyter labextension install @jupyterlab/htmlviewer-extension
RUN jupyter labextension install @jupyterlab/git
RUN pip install jupyterlab-git nbgitpuller
RUN jupyter serverextension enable --py jupyterlab_git --sys-prefix
RUN jupyter serverextension enable nbgitpuller --sys-prefix
#RUN jupyter labextension install jupyterlab-drawio
RUN jupyter lab build
#RUN pip uninstall -y tornado && \
#    pip install tornado==5.1.1
#    pip install tornado==4.5.3

# Run with remote kernel managers
CMD ["/usr/local/bin/start-nb2kg.sh"]

# Add local files as late as possible to avoid cache busting
ADD jupyter_notebook_config.py /etc/jupyter/jupyter_notebook_config.py
ADD start-nb2kg.sh /usr/local/bin/start-nb2kg.sh
