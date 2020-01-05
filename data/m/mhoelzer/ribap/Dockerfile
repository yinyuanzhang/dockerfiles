FROM ubuntu:xenial
ENV VERSION 0.1 

# init and install base dependencies needed
RUN apt-get update && apt-get install -y build-essential apt-utils build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev bioperl wget make g++ git rsync zip libopenmpi-dev default-jdk mcl cmake
    #rm /usr/bin/blastp /usr/bin/blastall /usr/bin/blastn /usr/bin/blastx /usr/bin/tblastn /usr/bin/tblastx /usr/bin/makeblastdb    

#RUN apt-get install -y cmake
RUN apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget make g++ git rsync zip libopenmpi-dev default-jdk mcl cmake

# install python3.7
RUN wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz 
RUN tar -xf Python-3.7.3.tar.xz
#RUN 
WORKDIR /Python-3.7.3
RUN ./configure --enable-optimizations && make build_all && make install
#RUN make
#RUN make install

# update pip3 and install perl and python modules
RUN pip3 install --upgrade pip && \
    if ! python3 -c "import networkx" &>/dev/null; then pip3 install networkx; fi && \
    if ! python3 -c "import docopt" &>/dev/null; then pip3 install docopt; fi && \
    if ! python3 -c "import Bio" &>/dev/null; then pip3 install BioPython; fi
RUN cpan Bio::Perl && cpan -f Bio::Roary

# remove ubuntu system blast binaries to not conflict with the blast version installed by the INSTALL.sh script later
#RUN rm /usr/bin/blastp /usr/bin/blastall /usr/bin/blastn /usr/bin/blastx /usr/bin/tblastn /usr/bin/tblastx /usr/bin/makeblastdb

# create new user 'dude' and home, switch from root to the dude
RUN useradd --create-home dude
WORKDIR /home/dude
USER dude

# copy scripts and further depedencies into the image
COPY INSTALL.sh .
COPY ribap.sh .
COPY scripts scripts
COPY strains strains
COPY web web

# run the full install script
RUN ./INSTALL.sh

# set paths
ENV PATH=/home/dude/ribap/bin:$PATH
#ENV PATH=$PATH:/home/dude
ENV PERL5LIB=/home/dude/ribap/lib:$PERL5LIB
ENV JAVA_HOME=/usr/bin
