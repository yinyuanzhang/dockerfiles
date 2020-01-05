#To build;
# docker build -t dock2hdm .
# to run;
# mkdir output
# docker run -v $(pwd)/output:/tohost -ti dock2hdm

# base image
FROM ubuntu:16.04

# some meta data
LABEL version=1.0
LABEL description="A docker container for 2HDMC"
LABEL author="Henry Day-Hall"

# install packages
RUN apt-get update && \
    apt-get -y install python2.7 ipython wget \
                       vim-nox nano make \
                       libgsl-dev g++ gfortran \
                       git python-ipdb tmux \
                       gedit
#RUN echo "alias vim=vim.tiny" >> ~/.bashrc

RUN apt -y install python-pip
RUN  pip install --upgrade pip

RUN pip install numpy matplotlib pyslha h5py lhapdf sklearn 

# fetch the packages
RUN  wget -O HiggsSignals.tar.gz https://higgsbounds.hepforge.org/downloads?f=HiggsSignals-2.2.3beta.tar.gz
RUN  wget -O 2HDMC.tar.gz https://2hdmc.hepforge.org/downloads/?f=2HDMC-1.7.0.tar.gz
RUN  wget -O SusHi.tar.gz https://sushi.hepforge.org/downloads/?f=SusHi-1.7.0.tar.gz
RUN  wget -O LHAPDF.tar.gz https://lhapdf.hepforge.org/downloads/?f=LHAPDF-6.2.3.tar.gz
RUN  wget -O HiggsBounds.tar.gz https://higgsbounds.hepforge.org/downloads?f=HiggsBounds-5.3.2beta.tar.gz
# import the alterations
RUN echo this line is needed to force a new git clone >> ./junk.txt
ARG CACHE_DATE=2022-08-15
RUN git clone https://tidefall@bitbucket.org/tidefall/higgspheno_docker.git && \
    mv higgspheno_docker/alterations ./                                     && \
    mv higgspheno_docker/scripts ./                                         && \
    mv higgspheno_docker/sample_data ./                                     && \
    yes | rm -r higgspheno_docker
## start making packages
RUN tar -xvf HiggsBounds.tar.gz                                             && \
    mkdir downloaded_packages                                               && \
    mv HiggsBounds.tar.gz downloaded_packages                               && \
    cd /HiggsBounds-5.3.2beta                                               && \
    # kill every print command
    python /scripts/silence_fortran.py                                      && \
    /bin/bash ./configure                                                   && \
    make                                                                    && \
    make libHB
RUN cd /                                                                    && \
    tar -xvf HiggsSignals.tar.gz                                            && \
    mv HiggsSignals.tar.gz downloaded_packages                              && \
    cd /HiggsSignals-2.2.3beta                                              && \
    # kill every print command
    python /scripts/silence_fortran.py                                      && \
    sed -i -e 's|HiggsBounds-5.3.1beta|HiggsBounds-5.3.2beta|' ./configure    && \
    /bin/bash ./configure                                                   && \
    make                                                                    && \
    make libHS
RUN cd /                                                                    && \
    tar -xvf 2HDMC.tar.gz                                                   && \
    mv 2HDMC.tar.gz downloaded_packages                                     && \
    cd /2HDMC-1.7.0                                                         && \
    cp /HiggsBounds-5.3.2beta/libHB.a ./lib/                                && \
    cp /HiggsSignals-2.2.3beta/libHS.a ./lib/                               && \
    sed -i -e 's/#CFLAGS+=-DHiggsBounds/CFLAGS+=-DHiggsBounds/' ./Makefile    && \
    sed -i -e 's/#LDFLAGS+=-L$(LIBDIR)/LDFLAGS+=-L$(LIBDIR)/' ./Makefile      && \
    sed -i -e 's/#SOURCES+=HBHS.cpp/SOURCES+=HBHS.cpp/' ./Makefile            && \
    # add some corrections (courtesy of Souad) 
    cp /alterations/Constraints.cpp /alterations/Constraints.h src/         && \
    cp /alterations/HBHS.cpp /alterations/HBHS.h src/                       && \
    # kill every print command
    sed -i -e 's|^\s*printf(|if(false) printf(|' src/*                           && \
    make 
RUN cd /                                                                    && \
    tar -xvf LHAPDF.tar.gz                                                  && \
    mv LHAPDF.tar.gz downloaded_packages                                    && \
    cd /LHAPDF-6.2.3                                                        && \
    /bin/bash ./configure                                                   && \
    make                                                                    && \
    make check                                                              && \
    make install
# also need pdf sets to do anything with this
RUN LHAPDF_SETS_DIR=/usr/local/share/LHAPDF                                 && \
    cd $LHAPDF_SETS_DIR                                                     && \
    wget --no-check-certificate https://www.hep.ucl.ac.uk/mmht/LHAPDF6/MMHT2014lo68cl.tar.gz  && \
    tar -xvf MMHT2014lo68cl.tar.gz                                          && \
    wget --no-check-certificate https://www.hep.ucl.ac.uk/mmht/LHAPDF6/MMHT2014nlo68cl.tar.gz  && \
    tar -xvf MMHT2014nlo68cl.tar.gz                                         && \
    wget --no-check-certificate https://www.hep.ucl.ac.uk/mmht/LHAPDF6/MMHT2014nnlo68cl.tar.gz  && \
    tar -xvf MMHT2014nnlo68cl.tar.gz
# going to make 2 versions of sushi, pipe and print
RUN cd /                                                                    && \
    tar -xvf SusHi.tar.gz                                                   && \
    mv SusHi.tar.gz downloaded_packages                                     && \
    cd /SusHi-1.7.0                                                         && \
    /bin/bash ./configure                                                   && \
    sed -i -e 's|^LHAPATH =.*$|LHAPATH = /usr/local/lib|' ./Makefile             && \
    sed -i -e 's|^2HDMCPATH =.*$|2HDMCPATH = /2HDMC-1.7.0|' ./Makefile           && \
    sed -i -e 's|^2HDMCVERSION =.*$|2HDMCVERSION = 1.7.0|' ./Makefile            && \
    sed -i -e 's|^HBPATH =.*$|HBPATH = /HiggsBounds-5.3.2beta|' ./Makefile       && \
    sed -i -e 's|^HBVERSION =.*$|HBVERSION = 5.3.2|' ./Makefile                  && \
    sed -i -e 's|^HSPATH =.*$|HSPATH = /HiggsSignals-2.2.3beta|' ./Makefile      && \
    sed -i -e 's|^HSVERSION =.*$|HSVERSION = 2.2.3|' ./Makefile                  && \
    # this one is a bit mysterious, but otherwise HB4/HS1 libraries get used
    sed -i -e 's|PREDEFLIBS := \${PREDEFLIBS} \${2HDMCPATH}/lib/lib2HDMC.a|PREDEFLIBS := ${PREDEFLIBS} ${2HDMCPATH}/lib/lib2HDMC.a ${2HDMCPATH}/lib/libHB.a ${2HDMCPATH}/lib/libHS.a|' ./Makefile && \
    # try to kill every print command
    python /scripts/silence_fortran.py                                         && \
    # that dosn't really work on SusHi, so make this change
    cp /alterations/sushi.F src/sushi.F                                        && \
    # make a copy of this
    cp -r /SusHi-1.7.0 /PipeSusHi                                              && \
    make predef=2HDMC
# now make the second version with the alterations
RUN cd /PipeSusHi                                                              && \
    cp /alterations/inputoutput.f /alterations/readslha.f src/sushi/           && \
    make predef=2HDMC
    
    

# now set up Rachid's script
RUN cp /scripts/InputTools.py /scripts/Rachid_ParamScan.py /2HDMC-1.7.0/    && \
    cp /scripts/Rachid_ParamScan.cpp /2HDMC-1.7.0/src/                      && \
    cd /2HDMC-1.7.0                                                         && \
    make Rachid_ParamScan

# set up my scripts
RUN cd /                                                                    && \ 
    cp /scripts/InputTools.py /scripts/MonteCarlo.py /2HDMC-1.7.0/          && \
    cp /scripts/InputTools.py /scripts/Scan.py /2HDMC-1.7.0/          && \
    cp /scripts/InputTools.py  /SusHi-1.7.0/                                && \
    cp /scripts/InputTools.py  /PipeSusHi/                                  && \
    cp /scripts/Data.py /2HDMC-1.7.0/                                       && \
    cp /scripts/Data.py /SusHi-1.7.0/                                       && \
    cp /scripts/Data.py /PipeSusHi/                                         && \
    cp /scripts/DiskWritingSusHiScan.py /SusHi-1.7.0/                       && \
    cp /scripts/RunSusHi.py /scripts/SusHiScan.py /PipeSusHi/               && \
    cp /scripts/Bounds.cpp /scripts/BRfromFile.cpp /2HDMC-1.7.0/src/        && \
    cp /scripts/pyslha2.py /scripts/souad_MC.py /                           && \
    cd /2HDMC-1.7.0                                                         && \
    make Bounds BRfromFile

# leave some instructions
RUN echo "echo" >> ~/.bashrc                                                                                                      && \
    echo "echo" >> ~/.bashrc                                                                                                      && \
    echo "echo 'To run the script please go to the directory 2HDMC-1.7.0'" >> ~/.bashrc                                           && \
    echo "echo 'and run > python Rachid_ParamScan.py'" >> ~/.bashrc                                                               && \
    echo "echo" >> ~/.bashrc                                                                                                      && \
    echo "echo 'Alternatively go to the directory 2HDMC-1.7.0'" >> ~/.bashrc                                                      && \
    echo "echo 'and run > python MonteCarlo.py'" >> ~/.bashrc                                                                     && \
    echo "echo 'and follow instructions on the prompt' " >> ~/.bashrc                                                             && \
    echo "echo" >> ~/.bashrc                                                                                                      && \
    echo "echo 'To extract the results to your computer, move them into the ./tohost/ folder' " >> ~/.bashrc                      && \
    echo "echo ' assuming you launched docker with ' " >> ~/.bashrc                                                               && \
    echo "echo '> run -v $(pwd)/output:/tohost -ti dock2hdm' " >> ~/.bashrc                                                       && \
    echo "echo" >> ~/.bashrc                                                                                                      && \
    echo "echo" >> ~/.bashrc
