FROM centos:7

LABEL maintainer="Sofiane Bendoukha <bendoukha@dkrz.de>"

USER root

# Install all OS dependencies for notebook server that starts but lacks all
# features (e.g., download as all possible file formats)

RUN yum -y update && \
    yum install -y epel-release && \
    yum install -yq \
    wget \
    make \
    bzip2 \
    ca-certificates \
    sudo \
    locales \
    davfs2 \
    fonts-liberation \
    gcc && \
    yum clean all

#RUN yum -y groupinstall "Development tools"

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen

# Install Tini
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.10.0/tini && \
    echo "1361527f39190a7338a0b434bd8c88ff7233ce7b9a4876f3315c22fce7eca1b0 *tini" | sha256sum -c - && \
    mv tini /usr/local/bin/tini && \
    chmod +x /usr/local/bin/tini

# Configure environment
ENV CONDA_DIR=/opt/conda \
    SHELL=/bin/bash \
    NB_USER=jovyan \
    NB_UID=1000 \
    NB_GID=100 \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8
ENV PATH=$CONDA_DIR/bin:$PATH \
    HOME=/home/$NB_USER

ADD fix-permissions /usr/local/bin/fix-permissions
# Create jovyan user with UID=1000 and in the 'users' group
# and make sure these dirs are writable by the `users` group.
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    mkdir -p $CONDA_DIR && \
    chown $NB_USER:$NB_GID $CONDA_DIR && \
    chmod g+w /etc/passwd /etc/group && \
    fix-permissions $HOME && \
    fix-permissions $CONDA_DIR

#RUN usermod -a -G davfs2 jovyan

USER $NB_UID

# Setup work directory for backward-compatibility
RUN mkdir /home/$NB_USER/work && \
    fix-permissions /home/$NB_USER

# Install conda as jovyan and check the md5 sum provided on the download site
ENV MINICONDA_VERSION=4.5.12 \
    CONDA_VERSION=4.6.7
RUN cd /tmp && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh && \
    echo "866ae9dff53ad0874e1d1a60b1ad1ef8 *Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh" | md5sum -c - && \
    /bin/bash Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh && \
    $CONDA_DIR/bin/conda config --system --prepend channels conda-forge && \
    $CONDA_DIR/bin/conda config --system --set auto_update_conda false && \
    $CONDA_DIR/bin/conda config --system --set show_channel_urls true && \
    $CONDA_DIR/bin/conda update --all --quiet --yes && \
    conda clean -tipsy && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# Install Tini
RUN conda install --quiet --yes 'tini=0.18.0' && \
    conda list tini | grep tini | tr -s ' ' | cut -d ' ' -f 1,2 >> $CONDA_DIR/conda-meta/pinned && \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# Install Jupyter Notebook and Hub
RUN conda install --quiet --yes \
    'proj4' \
    'notebook=5.7.8' \
    'basemap' \
    'tornado=5' \
    'ipython>=7.0.0' \
    'jupyterhub=1.0.0' \
    'jupyterlab>=1.0' && \
    conda clean -tipsy && \
    jupyter labextension install @jupyterlab/hub-extension@1.0.0 && \
    npm cache clean --force && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

ENV PROJ_LIB /opt/conda/share/proj/

USER root

EXPOSE 8888
WORKDIR $HOME

# Install PyOphidia
RUN pip install --upgrade pip &&\
    pip install \
        pyophidia \
        ipywidgets

# Configure container startup
ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.sh"]

# Add local files as late as possible to avoid cache busting
COPY start.sh /usr/local/bin/
COPY start-notebook.sh /usr/local/bin/
COPY mount-b2drop /usr/local/bin
COPY start-singleuser.sh /usr/local/bin/
COPY jupyter_notebook_config.py /etc/jupyter/
RUN fix-permissions /etc/jupyter/
RUN chown jovyan:users /usr/local/bin/mount-b2drop
RUN chmod +x /usr/local/bin/mount-b2drop

RUN wget --no-check-certificate https://download.ophidia.cmcc.it/rpm/1.5/ophidia-terminal-1.5.0-0.el7.centos.x86_64.rpm

RUN yum -y install ophidia-terminal-1.5.0-0.el7.centos.x86_64.rpm && \
    rm ophidia-terminal-1.5.0-0.el7.centos.x86_64.rpm

RUN echo "jovyan ALL = NOPASSWD: /bin/mount" >> /etc/sudoers

RUN echo "jovyan ALL = NOPASSWD: /usr/local/bin/mount-b2drop" >> /etc/sudoers

RUN echo "jovyan ALL = NOPASSWD: /sbin/mount.davfs" >> /etc/sudoers

RUN echo "jovyan ALL = NOPASSWD: /usr/bin/tee" >> /etc/sudoers

RUN echo "jovyan ALL = NOPASSWD: /usr/bin/chown" >> /etc/sudoers

RUN usermod -aG davfs2 jovyan

RUN setfacl -m u:jovyan:rw /etc/davfs2/secrets

RUN setfacl -m o::rw /etc/davfs2/secrets

RUN setfacl -m o::rw /etc/davfs2/davfs2.conf

RUN echo "use_locks 0" >> /etc/davfs2/davfs2.conf

RUN chmod 600 /etc/davfs2/secrets

#RUN chown jovyan:users /etc/davfs2/secrets

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID

RUN echo 'if [ $(whoami) == jovyan ]; then oph_term; exit' >> ~/.bashrc

RUN echo 'fi' >> ~/.bashrc

RUN mkdir ~/.ipython/ && mkdir ~/.ipython/profile_default

COPY ipython_config.py /home/jovyan/.ipython/profile_default/ipython_config.py

RUN chown -R jovyan: /home/jovyan/work

RUN touch /home/jovyan/work/.env

WORKDIR /home/jovyan/work

WORKDIR /home/jovyan

ADD notebook-extensions /home/jovyan

RUN jupyter nbextension install ecas --user

RUN jupyter nbextension enable ecas/publish/main

#RUN jupyter nbextension enable ecas/mount-b2drop/main

RUN mkdir /home/jovyan/work/conf

RUN touch /home/jovyan/work/conf/env

COPY mount-b2drop.py /home/jovyan/work/conf

COPY mount-your-b2drop.ipynb /home/jovyan/work/conf
