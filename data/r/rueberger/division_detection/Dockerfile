FROM tensorflow/tensorflow:latest-gpu

# System packages
RUN apt-get update && apt-get install -y curl git

# Install miniconda to /miniconda
RUN curl -LO http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
RUN bash Miniconda-latest-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda-latest-Linux-x86_64.sh
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda
RUN conda install ipython jupyter

# create expected dirs
WORKDIR /results
WORKDIR /logs
WORKDIR /research

ADD . /research/division_detection

# install augment
RUN pip install git+https://github.com/funkey/augment.git

# install pyklb
RUN conda install -c ilastik pyklb

RUN pip install -e division_detection/
