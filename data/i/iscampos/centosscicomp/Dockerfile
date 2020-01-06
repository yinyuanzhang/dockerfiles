
FROM centos:centos7

# This install compilers, scripters, and related tools

RUN yum -y groupinstall "Development Tools"

# Additional software for Math and MPI support

RUN yum -y install \
    wget \
    tcsh \
    texlive \
    texlive-preprint \
    emacs \
    which \
    gnuplot \
    gsl* \
    gmp* \
    mpfr* \
    openmpi*

# Setting some useful environment

RUN echo 'export GCC=gcc' > /etc/profile.d/scicomp.sh 
RUN echo 'export TZ=Europe/Rome' >> /etc/profile.d/scicomp.sh
RUN echo 'export PATH=$PATH:/usr/lib64/openmpi/bin:/usr/lib64/openmpi/lib' >> /etc/profile.d/scicomp.sh
RUN echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib64/openmpi/lib' >> /etc/profile.d/scicomp.sh
RUN echo 'export MPI_INCLUDE=/usr/include/openmpi-x86_64' >> /etc/profile.d/scicomp.sh

# Creating regular user developer

RUN /usr/sbin/useradd developer

RUN echo '/******************************************************************************/' > /etc/motd 
RUN echo '/**********   WELCOME TO CENTOS7 SCIENTIFIC COMPUTING CONTAINER   *************/' >> /etc/motd 
RUN echo '/                                                                              /' >> /etc/motd 
RUN echo '/ You might need to source the environment depending on the local directories  /' >> /etc/motd 
RUN echo '/ you mount (-v option) by typing: source /etc/profile.d/scicomp.sh            /' >> /etc/motd 
RUN echo '/                                                                              /' >> /etc/motd
RUN echo '/ If you detect problems please send an e-mail to: isabel.campos@csic.es       /' >> /etc/motd
RUN echo '/                                                                              /' >> /etc/motd
RUN echo '/******************************************************************************/' >> /etc/motd 

RUN echo '/usr/bin/cat /etc/motd' >> /etc/profile.d/scicomp.sh

CMD ["/bin/bash"]


# In case we need to install some OpenMPI version from sources

# In case we want to install openMPI from sources
#ENV OPENMPI_MAIN_V v2.0
#ENV OPENMPI_VERSION openmpi-2.0.1
#ENV OPENMPI_HOME /usr/local/$OPENMPI_VERSION

#WORKDIR /usr/local/src
#RUN mkdir -p $OPENMPI_HOME  
#RUN wget https://www.open-mpi.org/software/ompi/$OPENMPI_MAIN_V/downloads/$OPENMPI_VERSION.tar.gz
#RUN tar xzvf $OPENMPI_VERSION.tar.gz
#WORKDIR /usr/local/src/$OPENMPI_VERSION    
#RUN ./configure --prefix=$OPENMPI_HOME && make && make install
#WORKDIR /usr/local
#RUN ln -s $OPENMPI_VERSION openmpi
#RUN echo 'export PATH=$PATH:/usr/local/openmpi/bin' >> /etc/profile.d/scicomp.sh
#RUN echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/openmpi/lib' >> /etc/profile.d/scicomp.sh


