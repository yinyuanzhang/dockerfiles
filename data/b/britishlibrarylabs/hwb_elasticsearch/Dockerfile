FROM britishlibrarylabs/humanitiesworkbench

LABEL maintainer="Ben O'Steen <bosteen@gmail.com>"

USER $NB_USER

RUN conda install --quiet --yes \
    'elasticsearch==6.1.1' && \
    conda clean -tipsy && \
	fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

COPY load_metadata.ipynb /home/$NB_USER/

RUN jupyter trust /home/$NB_USER/load_metadata.ipynb

USER root

EXPOSE 8888
RUN fix-permissions /home/$NB_USER
	
USER $NB_USER