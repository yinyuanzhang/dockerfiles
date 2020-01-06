# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.

FROM phusion/baseimage
MAINTAINER Andrea Petri <apetri@phys.columbia.edu>

#Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

#This computer
ENV THIS="dock-lenstools"

#Refresh package cache
RUN apt-get update

########################################################
######Dependencies to install with apt-get##############
########################################################

#pkg-config, git, wget
RUN apt-get -y install pkg-config git wget

#git
RUN apt-get -y install git

#gfortran and OpenMPI
RUN apt-get -y install gfortran
RUN apt-get -y install libopenmpi-dev openmpi-bin

#Python, with headers and pip
RUN apt-get -y install python-dev python-pip 

#LAPACK,scipy,matplotlib
RUN apt-get -y install liblapack-dev python-scipy python-matplotlib

#Clone the LensTools repository, install it along with its requirements 
RUN git clone https://github.com/apetri/LensTools
RUN cd /LensTools ; git checkout docker-ubuntu ; pip install -r requirements.txt ; python setup.py install

#Install fftw2, necessary for the N-body codes
RUN cd /opt ; wget http://www.fftw.org/fftw-2.1.5.tar.gz ; tar -xf fftw-2.1.5.tar.gz ; cd fftw-2.1.5 ; ./configure --prefix=/usr/local --enable-type-prefix --enable-mpi ; make install

#Clone the LSST simulation repository for a test run
RUN git clone https://github.com/ColumbiaWeakLensing/LSST100parameters /TestRun
RUN cd /TestRun ; git checkout testrun

#Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*