# Use phusion/baseimage as base image
FROM phusion/baseimage:0.9.19

# Set environment variables the phusion way
RUN echo en_US.UTF-8 > /etc/container_environment/LANGUAGE
RUN echo en_US.UTF-8 > /etc/container_environment/LANG
RUN echo en_US.UTF-8 > /etc/container_environment/LC_ALL
RUN echo UTF-8 > /etc/container_environment/PYTHONIOENCODING

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

MAINTAINER Simon Frost <sdwfrost@gmail.com> and Mukarram Hossain <mukarram819@gmail.com>

## Set a default user. Available via runtime flag `--user docker`
RUN useradd docker \
	&& mkdir /home/docker \
	&& chown docker:docker /home/docker \
	&& mkdir /home/docker/programs \
	&& addgroup docker staff

RUN apt-get update -qq && \
  DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
 	build-essential \
	#default-jdk \
	#perl \
 	python3-dev \
	git \
	wget \
	cmake
	
# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Install GNU parallel
RUN curl -O http://ftp.gnu.org/gnu/parallel/parallel-20170122.tar.bz2 && \
  bzip2 -d parallel-20170122.tar.bz2 && \
  tar -xvf parallel-20170122.tar && \
  cd parallel-20170122 && \
  ./configure && make && make install && \
  cd ../ && \
  rm -r parallel-20170122.tar
  
# Install BLAST+
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/LATEST/ncbi-blast-2.6.0+-x64-linux.tar.gz && \
  tar -xvzf ncbi-blast-2.6.0+-x64-linux.tar.gz && \
  cp ../ncbi-blast-2.6.0+/bin/* ../bin/ && \
  rm ../ncbi-blast-2.6.0+-x64-linux.tar.gz
  
# Install the recent pip release
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
	python3 get-pip.py && \
	rm get-pip.py	&& \
	# Install numpy && \
	pip3 install numpy && \
	# Install Biopython && \
	pip3 install biopython && \
	# Install joblib && \
	pip3 install joblib && \
	# Install ETE3 && \
	pip3 install --upgrade ete3 && \
	pip3 install scipy

# Install CD-HIT
RUN cd /home/docker/programs && \
	git clone https://github.com/weizhongli/cdhit && \
	cd cdhit && \
	make && \
	cp cd-hit-est /usr/local/bin && \
	cp cd-hit /usr/local/bin && \
	rm -rf /home/docker/programs/cdhit

# Install IQ-TREE
RUN cd /home/docker/programs && \
	git clone https://github.com/Cibiv/IQ-TREE.git && \
	cd IQ-TREE && \
	mkdir build && \
	cd build && \
	cmake -DIQTREE_FLAGS=omp .. && \
	make && \
	cp iqtree-omp /usr/local/bin && \
	rm -rf /home/docker/programs/IQ-TREE

# Install MAFFT
RUN cd /home/docker/programs && \
	wget http://mafft.cbrc.jp/alignment/software/mafft-7.294-without-extensions-src.tgz && \
	tar zxvf mafft-7.294-without-extensions-src.tgz && \
	cd mafft-7.294-without-extensions/core && \
	make clean && \
	make && \
	make install && \
	rm /home/docker/programs/mafft-7.294-without-extensions-src.tgz && \
	rm -rf /home/docker/programs/mafft-7.294-without-extensions

# Install HMMER3
RUN cd /home/docker/programs && \
	wget http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2.tar.gz && \
	tar zxvf ./hmmer-3.1b2.tar.gz && \
	cd hmmer-3.1b2 && \
	./configure && \
	make && \
	make install && \
	rm /home/docker/programs/hmmer-3.1b2.tar.gz && \
	rm -rf /home/docker/programs/hmmer-3.1b2
	
# Install Pipelign
RUN cd /home/docker/programs && \
	git clone http://github.com/asmmhossain/pipelign.git && \
	cd pipelign && \
	chmod +x ./Pipelign.py && \
	cp ./Pipelign.py /usr/local/bin && \
	rm -rf /home/docker/programs/pipelign

  
  
# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#VOLUME ["data"]	
