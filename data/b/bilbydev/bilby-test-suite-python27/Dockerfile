FROM ubuntu:18.04

LABEL name="bilby Base Enterprise Linux 7" \
maintainer="Gregory Ashton <gregory.ashton@ligo.org>" \
date="20190104"

ENV PATH /opt/conda/bin:$PATH

# Install backend
RUN apt-get update --fix-missing \
&& apt-get install -y libglib2.0-0 libxext6 libsm6 libxrender1 libgl1-mesa-glx \
dh-autoreconf build-essential libarchive-dev wget curl git libhdf5-serial-dev

# Install python2.7
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda2-4.5.11-Linux-x86_64.sh -O ~/miniconda.sh && \
/bin/bash ~/miniconda.sh -b -p /opt/conda && \
rm ~/miniconda.sh && \
ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
echo "conda activate base" >> ~/.bashrc

# Install conda-installable programs
RUN conda install -y numpy scipy matplotlib pandas==0.23

RUN conda install -c conda-forge deepdish

# Install requirements
RUN pip install --upgrade pip \
&& pip install --upgrade setuptools \
&& pip install future \
pycondor>=0.5 \
configargparse \
flake8 \
mock \
pipenv \
coverage \
pytest-cov \
coverage-badge

# Install additional bilby requirements
RUN pip install corner lalsuite astropy gwpy theano

# Install samplers
RUN pip install cpnest dynesty emcee nestle ptemcee pymc3 pymultinest

# Install pymultinest requirements
RUN apt-get install -y libblas3 libblas-dev liblapack3 liblapack-dev \
libatlas3-base libatlas-base-dev cmake build-essential gfortran

# Install pymultinest
RUN git clone https://github.com/farhanferoz/MultiNest.git \
&& (cd MultiNest/MultiNest_v3.11_CMake/multinest && mkdir build && cd build && cmake .. && make)

ENV LD_LIBRARY_PATH $HOME/MultiNest/MultiNest_v3.11_CMake/multinest/lib:

# Install Polychord
RUN git clone https://github.com/PolyChord/PolyChordLite.git \
&& (cd PolyChordLite && make pypolychord  MPI= && python setup.py install)

# Install PTMCMCSampler
RUN git clone https://github.com/jellis18/PTMCMCSampler.git \
&& (cd PTMCMCSampler && python setup.py install)

# Add the ROQ data to the image
RUN mkdir roq_basis \
    && cd roq_basis \
    && wget https://git.ligo.org/lscsoft/ROQ_data/raw/master/IMRPhenomPv2/4s/B_linear.npy \
    && wget https://git.ligo.org/lscsoft/ROQ_data/raw/master/IMRPhenomPv2/4s/B_quadratic.npy \
    && wget https://git.ligo.org/lscsoft/ROQ_data/raw/master/IMRPhenomPv2/4s/fnodes_linear.npy \
    && wget https://git.ligo.org/lscsoft/ROQ_data/raw/master/IMRPhenomPv2/4s/fnodes_quadratic.npy \
    && wget https://git.ligo.org/lscsoft/ROQ_data/raw/master/IMRPhenomPv2/4s/params.dat \
