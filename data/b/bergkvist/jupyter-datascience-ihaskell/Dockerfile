FROM jupyter/datascience-notebook

USER root
RUN apt-get update -qq
RUN wget -qO- https://get.haskellstack.org/ | sh
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
        libzmq3-dev \
        libncurses-dev \
        pkg-config \
        netbase
USER jovyan
RUN stack --install-ghc --resolver lts-12.2 install ihaskell && ~/.local/bin/ihaskell install
RUN jupyter labextension install ihaskell_jupyterlab

CMD stack exec start-notebook.sh
