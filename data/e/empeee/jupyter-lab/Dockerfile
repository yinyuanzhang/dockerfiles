FROM continuumio/anaconda3:5.2.0

ENV JUPYTER_CONFIG_DIR="/opt/jupyterconfig"

# Apt installs
RUN apt update
RUN apt install -y octave octave-symbolic octave-miscellaneous gnuplot ghostscript
RUN apt clean

# Conda installs
RUN conda install -c conda-forge jupyterlab octave_kernel
RUN conda install mpld3 nodejs
RUN conda clean --all

# Pip installs
RUN pip install SchemDraw control tensorflow

# Jupyter installs
#RUN jupyter labextension install jupyterlab-drawio
#RUN jupyter labextension install jupyterlab-toc

EXPOSE 9999
CMD jupyter lab --ip=* --port 9999 --no-browser --allow-root --notebook-dir=/opt/notebooks
