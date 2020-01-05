FROM ubuntu:18.04
MAINTAINER dalzony@gmail.com

ENV SUNDIALS_INST /root/sundials/inst_sundials-3.1.1
ENV LD_LIBRARY_PATH $SUNDIALS_INST/lib

RUN apt-get -y update
RUN apt-get -y install python3 python3-dev
RUN apt-get -y install -y build-essential
RUN apt-get -y install python3-pip
RUN pip3 install numpy
RUN apt-get -y install gfortran
RUN apt-get -y install cmake ibopenblas-* libatlas-* liblapack-*

# Sundial & Odes
COPY sundials/inst_sundials-3.1.1 /root/sundials/inst_sundials-3.1.1
RUN pip3 install scikits.odes
RUN pip3 install nose

# matplotlib
# RUN python3 -m pip install -U matplotlib

# Cantera
RUN apt-get install -y aptitude
RUN apt-get install -y software-properties-common
RUN apt-add-repository ppa:speth/cantera
RUN aptitude update
RUN aptitude install -y cantera-python cantera-python3 cantera-dev
RUN pip3 install ipython matplotlib

RUN mkdir -p /root/code

#Python dependency
RUN pip3 install pandas