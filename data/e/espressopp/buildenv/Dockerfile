FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -q update -y
RUN apt-get -qq install -y build-essential mpich libmpich-dev libfftw3-dev libboost-all-dev git python-mpi4py cmake wget python-numpy ipython clang llvm ccache python-pip doxygen sphinx-common python-matplotlib graphviz texlive-latex-base texlive-latex-extra texlive-latex-recommended ghostscript libgromacs-dev latexmk libhdf5-dev python-h5py sudo
RUN wget -O /usr/bin/doxy-coverage https://raw.githubusercontent.com/alobbs/doxy-coverage/master/doxy-coverage.py
RUN chmod +x /usr/bin/doxy-coverage

RUN useradd -m -G sudo espressopp
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER espressopp
ENV PATH=/usr/lib/ccache:${PATH}${PATH:+:}
WORKDIR /home/espressopp
RUN pip install --user codecov coverxygen
