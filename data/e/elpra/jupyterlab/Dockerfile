FROM  python:3
LABEL maintainer="Tobias Baumann <tobias.baumann@elpra.de>"

RUN apt-get update && \
    apt-get -y install wget

RUN useradd -ms /bin/bash jupyter
USER jupyter

WORKDIR /home/jupyter
    
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && bash Miniconda3-latest-Linux-x86_64.sh -b

ENV PATH="/home/jupyter/miniconda3/bin:${PATH}"

RUN conda update -n base -c defaults conda
RUN conda install -c conda-forge -y jupyterlab nodejs nbconvert notebook jupytext matplotlib scipy imageio ipython pillow ipywidgets
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager

RUN jupyter lab paths

EXPOSE 8888

CMD [ "jupyter", "lab" ]
