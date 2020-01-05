FROM jupyter/scipy-notebook
LABEL maintainer="garaemon <garaemon@gmail.com>"

USER root
RUN apt-get update -y && \
    apt-get install --no-install-recommends -y libzmq3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_UID
RUN conda install --quiet --yes \
    tensorflow keras opencv && \
    pip install jupyter-emacskeys && \
    git clone https://github.com/notablemind/jupyter-nodejs.git && \
    cd jupyter-nodejs && \
    mkdir -p ~/.ipython/kernels/nodejs/ && \
    npm install && node install.js && \
    npm run build && npm run build-ext && \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR
