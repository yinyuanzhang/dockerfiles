FROM debian:stretch
LABEL maintainer="Chun-Jie Liu <chunjie-sam-liu@foxmail.com>"

ARG NB_USER="liucj"
ARG NB_UID="1000"
ARG NB_GID="100"

# Install all OS dependencies for notebook server that starts but lacks all
# features (e.g., download as all possible file formats)
# Configure environment
ENV DEBIAN_FRONTEND=noninteractive \
  CONDA_DIR=/opt/conda \
  SHELL=/bin/bash \
  NB_USER=$NB_USER \
  NB_UID=$NB_UID \
  NB_GID=$NB_GID \
  LC_ALL=en_US.UTF-8 \
  LANG=en_US.UTF-8 \
  LANGUAGE=en_US.UTF-8

ENV PATH=$CONDA_DIR/bin:$PATH \
  HOME=/home/$NB_USER \
  XDG_CACHE_HOME=/home/$NB_USER/.cache/

# Add a script that we will use to correct permissions after running certain commands

COPY fix-permissions start.sh start-notebook.sh start-singleuser.sh /usr/local/bin/
COPY jupyter_notebook_config.py /etc/jupyter/
COPY requirements.txt requirements.sys /tmp/

USER root
# Root Run
RUN apt-get update -qq \
  # install packages from requirements.sys
  && xargs apt-get -y --no-install-recommends install < /tmp/requirements.sys \
  && apt-get clean \
  && apt-get autoremove \
  && rm -rf /var/lib/apt/lists/* /tmp/requirements.sys \
  && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen \
  # Enable prompt color in the skeleton .bashrc before creating the default NB_USER
  && sed -i 's/^#force_color_prompt=yes/force_color_prompt=yes/' /etc/skel/.bashrc \
# Create NB_USER wtih name liucj user with UID=1000 and in the 'users' group
# and make sure these dirs are writable by the `users` group.
  && echo "auth requisite pam_deny.so" >> /etc/pam.d/su \
  && sed -i.bak -e 's/^%admin/#%admin/' /etc/sudoers \
  && sed -i.bak -e 's/^%sudo/#%sudo/' /etc/sudoers \
  && useradd $NB_USER -b ${HOME} -d ${HOME} -g ${NB_GID} -m -s /bin/bash -N -u $NB_UID \
  && mkdir -p $CONDA_DIR \
  && echo "export PATH=$CONDA_DIR/bin/:\$PATH" >> ${HOME}/.bashrc \
  && chown $NB_USER:$NB_GID $CONDA_DIR \
  && chmod g+w /etc/passwd \
  && fix-permissions $HOME \
  && fix-permissions "$(dirname $CONDA_DIR)" \
  && fix-permissions /etc/jupyter/

USER $NB_UID
WORKDIR $HOME
# User run
  # Setup work directory for backward-compatibility
RUN mkdir /home/$NB_USER/jupyter-workspace \
  # install miniconda and config miniconda
  && cd /tmp \
  && wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
  && /bin/bash Miniconda3-latest-Linux-x86_64.sh -f -b -p $CONDA_DIR \
  && rm Miniconda3-latest-Linux-x86_64.sh \
  && export PATH=$CONDA_DIR/bin/:$PATH \
  && conda config --system --prepend channels conda-forge \
  && conda config --system --set auto_update_conda false \
  && conda config --system --set show_channel_urls true \
  && conda list python | grep '^python ' | tr -s ' ' | cut -d '.' -f 1,2 | sed 's/$/.*/' >> $CONDA_DIR/conda-meta/pinned \
  && conda install --quiet --yes 'tini' \
  && conda list tini | grep tini | tr -s ' ' | cut -d ' ' -f 1,2 >> $CONDA_DIR/conda-meta/pinned \
  # install packages in the requirements.txt
  && conda install --quiet --yes --file /tmp/requirements.txt \
  && conda update --all --quiet --yes \
  && conda clean --all -f -y \
  && jupyter notebook --generate-config \
  # Activate ipywidgets extension in the environment that runs the notebook server
  && jupyter nbextension enable --py widgetsnbextension --sys-prefix \
  && jupyter labextension install @jupyter-widgets/jupyterlab-manager \
  && jupyter labextension install jupyterlab_bokeh \
  && git clone https://github.com/PAIR-code/facets.git \
  && cd facets \
  && jupyter nbextension install facets-dist/ --sys-prefix \
  && cd && rm -rf /tmp/facets \
  # Import matplotlib the first time to build the font cache.
  && MPLBACKEND=Agg python -c "import matplotlib.pyplot" \
  # remote caches
  && rm -rf $CONDA_DIR/share/jupyter/lab/staging \
  && rm -rf /home/$NB_USER/.cache/yarn \
  && rm -rf /home/$NB_USER/.node-gyp \
  && fix-permissions $CONDA_DIR \
  && fix-permissions /home/$NB_USER

EXPOSE 8888

# Configure container startup
ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.sh"]

# Switch back to liucj to avoid accidental container runs as root
USER $NB_UID