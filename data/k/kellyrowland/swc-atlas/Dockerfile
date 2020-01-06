# Choose your desired base image
FROM jupyter/scipy-notebook:latest

# Create a Python 2.x environment using conda including at least the ipython kernel
# and the kernda utility. Add any additional packages you want available for use
# in a Python 2 notebook to the first line here (e.g., pandas, matplotlib, etc.)
RUN conda create --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 ipython \
    ipykernel kernda scipy pytest && \
    conda clean --all -f -y

RUN ln -s $CONDA_DIR/envs/python2/bin/python $CONDA_DIR/bin/python2
RUN ln -s $CONDA_DIR/envs/python2/bin/ipython $CONDA_DIR/bin/ipython2
RUN ln -s $CONDA_DIR/envs/python2/bin/pytest $CONDA_DIR/bin/pytest

USER root

RUN apt-get update && apt-get install -y vim

# Create a global kernelspec in the image and modify it so that it properly activates
# the python2 conda environment.
RUN $CONDA_DIR/envs/python2/bin/python -m ipykernel install && \
$CONDA_DIR/envs/python2/bin/kernda -o -y /usr/local/share/jupyter/kernels/python2/kernel.json

USER $NB_USER
