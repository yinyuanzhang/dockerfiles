FROM ubuntu:16.04

ADD entrypoint.sh /
ADD openssl.conf /opt/

#Install yarn and NodeJS
RUN apt-get -qq update -y
RUN apt-get install -y unzip wget curl tar bzip2 software-properties-common git vim 
#RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
#RUN apt-get install -y nodejs
#RUN npm install yarn -g

# Install Java 8
ENV JAVA_HOME /opt/jdk1.8.0_191
ENV PATH $PATH:/opt/jdk1.8.0_191/bin:/opt/jdk1.8.0_191/jre/bin:/etc/alternatives:/var/lib/dpkg/alternatives

RUN cd /opt && wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u191-b12/2787e4a523244c269598db4e85c51e0c/jdk-8u191-linux-x64.tar.gz" &&\
   tar xzf jdk-8u191-linux-x64.tar.gz && rm -rf jdk-8u191-linux-x64.tar.gz

RUN echo 'export JAVA_HOME="/opt/jdk1.8.0_191"' >> ~/.bashrc && \
    echo 'export PATH="$PATH:/opt/jdk1.8.0_191/bin:/opt/jdk1.8.0_191/jre/bin"' >> ~/.bashrc && \
    bash ~/.bashrc && cd /opt/jdk1.8.0_191/ && update-alternatives --install /usr/bin/java java /opt/jdk1.8.0_191/bin/java 1
    
#Add Java Security Policies
RUN curl -L -C - -b "oraclelicense=accept-securebackup-cookie" -O http://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip && \
   unzip jce_policy-8.zip
RUN cp UnlimitedJCEPolicyJDK8/US_export_policy.jar /opt/jdk1.8.0_191/jre/lib/security/ && cp UnlimitedJCEPolicyJDK8/local_policy.jar /opt/jdk1.8.0_191/jre/lib/security/
RUN rm -rf UnlimitedJCEPolicyJDK8

# Install Spark 2.3.0
RUN cd /opt && wget https://archive.apache.org/dist/spark/spark-2.3.0/spark-2.3.0-bin-hadoop2.7.tgz && \
   tar xzvf /opt/spark-2.3.0-bin-hadoop2.7.tgz && \
   rm  /opt/spark-2.3.0-bin-hadoop2.7.tgz 
   
# Spark pointers for Jupyter Notebook
ENV SPARK_HOME /opt/spark-2.3.0-bin-hadoop2.7
ENV R_LIBS_USER $SPARK_HOME/R/lib:/opt/conda/envs/ir/lib/R/library:/opt/conda/lib/R/library
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.8.2.1-src.zip

ENV PATH $PATH:/$SPARK_HOME/bin/


#ENV R_LIBS_USER /opt/conda/envs/ir/lib/R/library:/opt/conda/lib/R/library

# Create additional files in the DataLake
RUN chmod 777 /entrypoint.sh

# Setup Miniconda
ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH

RUN cd /opt && \
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \ 
    /bin/bash Miniconda3-latest-Linux-x86_64.sh  -b -p $CONDA_DIR && \
     rm -rf Miniconda3-latest-Linux-x86_64.sh

RUN export PATH=$PATH:$CONDA_DIR/bin

# Install Jupyter notebook 
RUN $CONDA_DIR/bin/conda install --yes \
    'notebook>=5.6.0' && \
    $CONDA_DIR/bin/conda clean -yt
    
# Install JupyterHub
RUN $CONDA_DIR/bin/conda install -y -c conda-forge jupyterhub && \
    $CONDA_DIR/bin/conda clean -yt
    
#RUN $CONDA_DIR/bin/conda install -c conda-forge nb_conda
#RUN $CONDA_DIR/bin/python -m nb_conda_kernels.install --disable --prefix=$CONDA_DIR && \
#    $CONDA_DIR/bin/conda clean -yt

#Install Scala Spark kernel
ENV SBT_VERSION 0.13.11
ENV SBT_HOME /usr/local/sbt
ENV PATH ${PATH}:${SBT_HOME}/bin
    
#Install Python3 packages
RUN cd /root && $CONDA_DIR/bin/conda install --yes \
    'ipywidgets' \
    'pandas' \
    'matplotlib' \
    'scipy' \
    'seaborn' \
    'scikit-learn' && \
    $CONDA_DIR/bin/conda clean -yt
    
RUN $CONDA_DIR/bin/conda config --set auto_update_conda False

#RUN CONDA_VERBOSE=3 $CONDA_DIR/bin/conda create --yes -p $CONDA_DIR/envs/python3 python=3.5 ipython ipywidgets pandas matplotlib scipy seaborn scikit-learn
#RUN bash -c '. activate $CONDA_DIR/envs/python3 && \
 #   python -m ipykernel.kernelspec --prefix=/opt/conda && \
 #   . deactivate'
    
#RUN wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 -O /root/jq-linux64

#RUN chmod +x /root/jq-linux64
#RUN /root/jq-linux64 --arg v "$CONDA_DIR/envs/python3/bin/python"         '.["env"]["PYSPARK_PYTHON"]=$v' /opt/conda/share/jupyter/kernels/python3/kernel.json > /tmp/kernel.json &&   \
#    mv /tmp/kernel.json /opt/conda/share/jupyter/kernels/python3/kernel.json

#Install R kernel and set up environment
#RUN $CONDA_DIR/bin/conda config --add channels r
#RUN $CONDA_DIR/bin/conda install --yes -c r r-essentials r-base r-irkernel r-irdisplay r-ggplot2 r-repr r-rcurl
#RUN $CONDA_DIR/bin/conda create --yes  -n ir -c r r-essentials r-base r-irkernel r-irdisplay r-ggplot2 r-repr r-rcurl

#Configure Scala kernel
RUN mkdir -p /opt/conda/share/jupyter/kernels/scala
COPY kernel.json /opt/conda/share/jupyter/kernels/scala/

RUN apt-get install -y make

RUN cd /tmp && \
    wget "http://repo.bigstepcloud.com/bigstep/datalab/sbt-0.13.11.tgz" -O /tmp/sbt-0.13.11.tgz && \
    tar -xvf /tmp/sbt-0.13.11.tgz -C /usr/local && \
    echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built && \
    git clone https://github.com/apache/incubator-toree.git && \
    cd incubator-toree && \
    git checkout cc8bf2a561d87c289981298ab594d2ea851ad1ed && \
    make dist SHELL=/bin/bash APACHE_SPARK_VERSION=2.3.0 SCALA_VERSION=2.11 && \
    mv /tmp/incubator-toree/dist/toree /opt/toree-kernel && \
    chmod +x /opt/toree-kernel && \
    rm -rf /tmp/incubator-toree && \
    wget http://repo.bigstepcloud.com/bigstep/datalab/toree-assembly-0.3.0.dev1-incubating-SNAPSHOT.jar -O /opt/toree-kernel/lib/toree-assembly-0.3.0.dev1-incubating-SNAPSHOT.jar

RUN cd /opt && \
    wget http://repo.uk.bigstepcloud.com/bigstep/bdl/bigstepdatalake-1.0-SNAPSHOT-bin.tar.gz && \
    tar -xzvf bigstepdatalake-1.0-SNAPSHOT-bin.tar.gz && \
    rm -rf /opt/bigstepdatalake-1.0-SNAPSHOT-bin.tar.gz && \
    export PATH=/opt/bigstepdatalake-1.0-SNAPSHOT/bin:$PATH
    
RUN pip install py4j && \
    pip install pyspark

#        JupyterHub 
EXPOSE   8000     4040 4041 4042 4043 4044 4045  4046 4047 4048 4049

ENTRYPOINT ["/entrypoint.sh"]
