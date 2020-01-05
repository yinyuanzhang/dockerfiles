FROM jazzdd/alpine-flask:python3
MAINTAINER Sang Venkatraman <sang@driveclutch.com>


RUN apk update && apk add build-base postgresql-dev libffi-dev #needed for sqlalchemy to be installed correctly
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h #needed for numpy to be installed correctly
RUN apk add gfortran \
            libgfortran

COPY libs/* /tmp/
RUN source /tmp/blas.sh
RUN source /tmp/lapack.sh

#ENV BLAS /usr/local/lib/libfblas.a
#ENV LAPACK /usr/local/lib/liblapack.a

COPY app/pip_install_*.txt /app/
RUN BLAS=~/src/BLAS/libfblas.a LAPACK=~/src/lapack-3.5.0/liblapack.a pip3 install -r pip_install_phase1.txt
RUN BLAS=~/src/BLAS/libfblas.a LAPACK=~/src/lapack-3.5.0/liblapack.a pip3 install -r pip_install_phase2.txt
