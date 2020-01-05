FROM nanjiang/common-ubuntu
LABEL maintainer "Alexander Kvist (akv@kth.se), Nanjiang Shu (nanjiang.shu@nbis.se)"
LABEL version "1.0"


#================================
# Install basics
#===============================
RUN apt-get  update -y
RUN apt-get install -y apt-utils  \
                       curl wget vim tree bc git \
                       python python-dev python-pip \
                       build-essential \
                       libxml2-dev libxslt1-dev libsqlite3-dev zlib1g-dev  \
                       python-lxml

#================================
#  Add pathopred source code
#===============================
WORKDIR /app
# add the source code to WORKDIR/app
ADD . ./pathopred
RUN mkdir /home/download /scratch /static

#================================
# Install blast 2.7.1+
#===============================
RUN cd /home/download && \
        wget --quiet ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.7.1/ncbi-blast-2.7.1+-x64-linux.tar.gz -O  ncbi-blast-2.7.1+-x64-linux.tar.gz  && \
        tar -xvzf  ncbi-blast-2.7.1+-x64-linux.tar.gz  && \
        mv ncbi-blast-2.7.1+  /app/blast

#================================
# Update PATH with blast
#===============================
ENV PATH /app/blast/bin:$PATH

#================================
# Install python package 
#===============================
RUN pip install --upgrade pip
RUN pip install biopython==1.70 \
                matplotlib==1.5.3 \
                numpy==1.14.5  \
                scipy==0.18.1  \
                pandas==0.23.4 \
                goatools==0.8.4 \
                tables==3.4.4   \
                Cython==0.28.5 \
                tqdm \
                tensorflow==1.10.0 \
                keras==2.2.2 \
                h5py==2.8.0



#================================
# Setting keras configuration
#===============================
RUN mkdir -p /home/user/.keras

#===========================
# Prepare cython script
#==================
WORKDIR ./pathopred
RUN python setup.py build_ext -i
WORKDIR /app

#================================
# Clean
#===============================
RUN rm -rf /home/download

# This will change the ownership of the folder /app to be the user that starts the docker container. Disable it unless necessary
# ENV USER_DIRS "/app"

RUN export LC_ALL="en_US.UTF-8"

CMD ["/bin/bash" ]
