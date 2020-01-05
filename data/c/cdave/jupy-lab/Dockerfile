from jupyter/scipy-notebook:59904dd7776a

# Add extensions to make JupyterLab a thing
RUN jupyter labextension install jupyterlab_vim

# Nice to haves
RUN pip --no-cache-dir install \
        tifffile \ 
        czifile 

RUN conda install --quiet --yes \
    'opencv' \
    'scikit-image' \ 
    'tqdm' \ 
    'pathos'

