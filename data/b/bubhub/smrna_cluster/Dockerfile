FROM python:3.6-stretch

RUN apt update -y
RUN apt upgrade -y

# install numpy and scipy separately because they have to be
# compiled before other dependencies that need them
RUN pip install --trusted-host pypi.python.org numpy scipy cutadapt networkx boto3 botocore biopython

# install cd-hit
RUN wget https://github.com/weizhongli/cdhit/releases/download/V4.8.1/cd-hit-v4.8.1-2019-0228.tar.gz
RUN tar zxf cd-hit-v4.8.1-2019-0228.tar.gz
RUN (cd cd-hit-v4.8.1-2019-0228; make; cp cd-hit cd-hit-est cd-hit-div /usr/bin)

# clone and install smrnatk (added smrnatk python files here, might not need this)
#RUN git clone https://bitbucket.org/bubioinformaticshub/smrnatk .
#RUN (cd smrnatk; python setup.py)

# make bind points for singularity
RUN mkdir /cromwell-executions/

# install DNApi
RUN git clone https://github.com/jnktsj/DNApi.git && cd DNApi && python setup.py install

# install sratoolkit
RUN wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.9.6-1/sratoolkit.2.9.6-1-ubuntu64.tar.gz
RUN tar zxf sratoolkit.2.9.6-1-ubuntu64.tar.gz 
RUN cp -r sratoolkit.2.9.6-1-ubuntu64/bin/* /usr/bin

# install muscle (multiple sequence alignment)
RUN wget http://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux64.tar.gz
RUN tar -zxvf muscle3.8.31_i86linux64.tar.gz && rm -f muscle3.8.31_i86linux64.tar.gz
RUN mv muscle3.8.31_i86linux64 muscle && cp muscle /usr/bin

COPY . /smrna_cluster
RUN (cd /smrna_cluster; python setup.py install)
