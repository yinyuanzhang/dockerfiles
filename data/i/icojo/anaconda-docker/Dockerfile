# We will use Ubuntu for our image
FROM ubuntu
# Updating Ubuntu packages
RUN apt-get update && yes|apt-get upgrade
# Adding wget and bzip2
RUN apt-get install -y wget bzip2

ENV ANACONDA_VERSION 3-5.2.0

RUN wget https://repo.anaconda.com/archive/Anaconda$ANACONDA_VERSION-Linux-x86_64.sh

RUN bash Anaconda$ANACONDA_VERSION-Linux-x86_64.sh -b

# Set path to conda
ENV PATH /root/anaconda3/bin:$PATH
# Updating Anaconda packages
RUN conda update conda
RUN conda update anaconda
RUN conda update --all

# Configuring access to Jupyter
RUN mkdir /opt/notebooks
RUN jupyter notebook --generate-config --allow-root
RUN echo "c.NotebookApp.password = u'sha1:6a3f528eec40:6e896b6e4828f525a6e20e5411cd1c8075d68619'" >> /root/.jupyter/jupyter_notebook_config.py
# Jupyter listens port: 8888
EXPOSE 8888

# Run Jupytewr notebook as Docker main process
CMD ["jupyter", "notebook", "--allow-root", "--notebook-dir=/opt/notebooks", "--ip='*'", "--port=8888", "--no-browser"]
