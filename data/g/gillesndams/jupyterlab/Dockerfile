# ipython notebook Dockerfile
FROM ubuntu
MAINTAINER robertondame@gmail.com

RUN apt update && apt -y upgrade && apt install -y python python3

RUN apt-get update && apt-get install -y -q \
        gfortran \
        curl \
        libfreetype6-dev \
        libxft-dev \
        libopenblas-dev \
        liblapack-dev \
        unzip

RUN apt-get install -y python-pip python3-pip

RUN pip3 install --upgrade pip && pip2 install --upgrade pip

RUN pip3 install cython numpy pandas scipy scikit-learn matplotlib \
        seaborn \
        sympy \
        patsy \
        statsmodels \
        pymongo \
        openpyxl \
        xlrd \
        arrow \
        "tornado>=4.0.0,<5.0.0" \
        azure \
        boto \
        jupyter notebook

RUN pip2.7 install cython numpy pandas scipy scikit-learn matplotlib \
        seaborn \
        sympy \
        patsy \
        statsmodels \
        pymongo \
        openpyxl \
        xlrd \
        arrow \
        "tornado>=4.0.0,<5.0.0" \
        azure \
        boto \
        jupyter notebook


# Install kernel python2 and python3
RUN python2 -m pip install ipykernel && \
    python2 -m ipykernel install --user

RUN python3 -m pip install ipykernel && \
    python3 -m ipykernel install --user


# R pre-requisities
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    gfortran \
    libxml2-dev \
    gcc && apt-get clean && \
    rm -rf /var/lib/apt/lists/*
# R Kernel and RStudio 
RUN apt-get update
RUN apt-get install -y \
software-properties-common \
python3-software-properties 

RUN add-apt-repository -y ppa:marutter/rrutter
RUN apt-get update
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get install -y \
r-base-core \
r-base \
r-base-dev 

# Finelize the R install kernel:
RUN R -e "install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest'), repos = 'http://cran.us.r-project.org')"
RUN apt update && apt install -y libcurl4-openssl-dev libssl-dev
RUN R -e "install.packages(c('devtools'), repos = 'http://cran.us.r-project.org')"
RUN apt install -y git 
RUN R -e "devtools::install_github('IRkernel/IRkernel')"

#RUN R -e "install.packages(c('ggplot2', 'plyr', 'reshape2', 'RColorBrewer', 'scales','grid', 'wesanderson', 'bigrquery','googleCloudStorageR','rmarkdown','flexdashboard'), repos='http://cran.us.r-project.org', dependencies=TRUE)"
RUN R -e "IRkernel::installspec()"

# Install spark 
ENV  APACHE_SPARK_VERSION 2.4.0
RUN add-apt-repository ppa:openjdk-r/ppa
RUN apt-get update
RUN  apt-get install -y --no-install-recommends openjdk-8-jre-headless wget 
RUN  wget -qO - http://mirrors.standaloneinstaller.com/apache/spark/spark-${APACHE_SPARK_VERSION}/spark-${APACHE_SPARK_VERSION}-bin-hadoop2.7.tgz |tar -xz -C /usr/local/
RUN  cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop2.7 spark
ENV  SPARK_HOME /usr/local/spark

# Install kernel pyspark 
RUN mkdir /usr/local/share/jupyter/kernels/pyspark
ADD kernel.json /usr/local/share/jupyter/kernels/pyspark/

## For ipython notebook
VOLUME /data
WORKDIR /data
EXPOSE 8888

# You can mount your own SSL certs as necessary here
ENV PEM_FILE /key.pem

# Default BASEURL is jupyterogen ; set a BASEURL while docker run to change that 
ENV BASEURL jupyterogen 

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs
RUN apt-get install -y gcc g++ make python-magic python3-magic

RUN curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
     echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
     apt-get update && apt-get -y install yarn

ENV SHELL /bin/bash
RUN pip install toree pixiedust pyyaml ipympl

RUN apt install -y texlive texlive-latex-extra texlive-xetex pandoc

# Install go
RUN wget -qO - https://dl.google.com/go/go1.11.linux-amd64.tar.gz | tar -xz -C /usr/local/
RUN mkdir /root/go
ENV PATH $PATH:/usr/local/go/bin
ENV GOPATH=/root/go
RUN apt install -y git libzmq3-dev inkscape
RUN go get -u github.com/gopherdata/gophernotes
RUN mkdir /usr/local/share/jupyter/kernels/gophernotes
RUN cp $GOPATH/src/github.com/gopherdata/gophernotes/kernel/* /usr/local/share/jupyter/kernels/gophernotes
ENV PATH $PATH:/root/go/bin

RUN jupyter toree install --spark_home=${SPARK_HOME} --interpreters=Scala,SQL,SparkR --kernel_name='Spark' 
RUN pip3 install jupyterlab && pip2 install jupyterlab
RUN pip2 install ipympl && pip3 install ipympl 
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-matplotlib
ADD ipython.sh /
RUN chmod u+x /ipython.sh
ADD banner.txt /
CMD ["/ipython.sh"]
