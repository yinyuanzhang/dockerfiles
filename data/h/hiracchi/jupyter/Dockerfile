FROM hiracchi/ubuntu-ja:18.04.1

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/hiracchi/docker-jupyter" \
      org.label-schema.version=$VERSION \
      maintainer="Toshiyuki Hirano <hiracchi@gmail.com>"

ARG NGLVIEW_VER=1.1.7
ARG WORKDIR="/work"
# ARG MINICONDA_URL="https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh"
ARG MINICONDA_URL="https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh"


# setup packages ===============================================================
RUN set -x \
  && apt-get update \
  && apt-get install -y \
     git wget \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# install conda ================================================================
# RUN set -x \
#   && wget "${MINICONDA_URL}" -O /tmp/miniconda.sh \
#   && bash /tmp/miniconda.sh -b -p /opt/miniconda \
#   && rm /tmp/miniconda.sh


# ENV PATH="${PATH}:/opt/miniconda/bin"
# RUN set -x \
#   && conda config --add channels defaults \
#   && conda config --add channels conda-forge \
#   && conda config --add channels bioconda


# # "numpy" should be at the end of the list, in order to avoid errors on the NGLView
# RUN set -x \
#   && conda update conda \
#   && conda create --name jupyter2 python=2 \
#   && conda create --name jupyter3 python=3 

# # python2
# RUN set -x \
#   && . /opt/miniconda/etc/profile.d/conda.sh \
#   && conda activate jupyter2 \
#   && conda install msgpack-c msgpack-python pyyaml \
#     numpy scipy sympy pandas biopandas xlrd \
#     matplotlib bokeh \
#     scikit-learn \
#     h5py tqdm \
#     requests beautifulsoup4 \
#     notebook ipykernel \
#     ipywidgets \
#     jupyter_contrib_nbextensions \
#     jupyter_nbextensions_configurator \
#     nglview=${NGLVIEW_VER} \
#   && jupyter-nbextension enable nglview --py --sys-prefix \
#   && python -m ipykernel install \
#   && find /opt -name __pycache__ | xargs rm -r \
#   && rm -rf /opt/miniconda/pkgs/* \
#   && conda env export > myenv.yml

# # python3
# RUN set -x \
#   && . /opt/miniconda/etc/profile.d/conda.sh \
#   && conda activate jupyter3 \
#   && conda install msgpack-c msgpack-python pyyaml \
#     numpy scipy sympy pandas biopandas xlrd \
#     matplotlib bokeh \
#     scikit-learn \
#     h5py tqdm \
#     requests beautifulsoup4 \
#     notebook ipykernel \
#     ipywidgets \
#     jupyter_contrib_nbextensions \
#     jupyter_nbextensions_configurator \
#     nglview=${NGLVIEW_VER} \
#   && jupyter-nbextension enable nglview --py --sys-prefix \
#   && python -m ipykernel install \
#   && find /opt -name __pycache__ | xargs rm -r \
#   && rm -rf /opt/miniconda/pkgs/* 

# # confirm
# RUN set -x \
#   && . /opt/miniconda/etc/profile.d/conda.sh \
#   && conda info -e \
#   && conda activate jupyter2 \
#   && jupyter kernelspec list


# -----------------------------------------------------------------------------
# System Python3
# -----------------------------------------------------------------------------
RUN set -x \
  && apt-get update \
  && apt-get install -y \
    build-essential \
    python3-dev python3-pip \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN set -x \
  && pip3 install --no-cache-dir \
    msgpack-python pyyaml \
    numpy scipy sympy pandas xlrd xlwt \
    matplotlib  bokeh \
    scikit-learn \
    h5py tqdm \
    requests beautifulsoup4 \
    jupyter \
    jupyter_contrib_nbextensions \
    jupyter_nbextensions_configurator \
    ipywidgets \
    pytraj \
    nglview==${NGLVIEW_VER}

RUN set -x \
  && jupyter contrib nbextension install \
  && jupyter nbextensions_configurator enable \
  && jupyter nbextension enable widgetsnbextension \
  && jupyter-nbextension enable nglview 


# -----------------------------------------------------------------------------
# for JupyterLab 
# -----------------------------------------------------------------------------
# RUN set -x \
#   && apt-get update \
#   && apt-get install -y \
#     nodejs npm \
#   && apt-get clean \
#   && rm -rf /var/lib/apt/lists/*
# RUN set -x \
#   && pip3 install --no-cache-dir \
#     jupyterlab \
#   && jupyter labextension install @jupyter-widgets/jupyterlab-manager


# -----------------------------------------------------------------------------
# setup dirs 
# -----------------------------------------------------------------------------
RUN set -x \
  && mkdir -p "${WORKDIR}" \
  && chmod 777 "${WORKDIR}" \
  && mv /root/.jupyter "${WORKDIR}" \
  && ln -s "${WORKDIR}/.jupyter" /root/.jupyter 


# -----------------------------------------------------------------------------
# entrypoint
# -----------------------------------------------------------------------------
COPY jupyter_notebook_config.py /jupyter_notebook_config.py
WORKDIR ${WORKDIR}
ENV WORKDIR="${WORKDIR}"
VOLUME ${WORKDIR}
EXPOSE 8888

COPY run-jupyter.sh run-jupyterlab.sh /usr/local/bin/
COPY make-jupyter-password.sh /usr/local/bin/
RUN set -x \
  && chmod +x /usr/local/bin/*.sh
CMD ["/usr/local/bin/run-jupyter.sh"]
