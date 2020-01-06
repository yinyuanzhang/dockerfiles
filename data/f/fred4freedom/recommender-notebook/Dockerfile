FROM bde2020/spark-master:2.3.0-hadoop2.7


#####################################################
# Install standard packages needed for development 
# environment

RUN apt-get update && \
    apt-get install -y apt-transport-https && \
    apt-get install -y build-essential libbz2-dev libssl-dev libreadline-dev libsqlite3-dev tk-dev && \
    apt-get install -y libpng-dev libfreetype6-dev python3-dev zip p7zip && \
    apt-get install -y libgoogle-glog-dev libgflags-dev liblapack-dev && \
    apt-get install -y nano vim && \
    apt-get clean


#####################################################
# Install python 
ENV PYTHON3_VERSION=3.6.6
ENV PYTHON2_VERSION=2.7.15
RUN curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash && \
    export PATH="/root/.pyenv/bin:$PATH" && \
    pyenv update && \
    echo 'eval "$(pyenv init -)"' >> /root/.profile && \ 
    echo 'eval "$(pyenv virtualenv-init -)"' >> /root/.profile && \ 
    echo 'eval "$(pyenv init -)"' >> /root/.bashrc && \ 
    echo 'eval "$(pyenv virtualenv-init -)"' >> /root/.bashrc && \     
    pyenv install ${PYTHON3_VERSION} && \
    pyenv install ${PYTHON2_VERSION} && \
    pyenv global ${PYTHON3_VERSION}
ENV PATH="/root/.pyenv/bin:${PATH}"

#####################################################
# Define environment variables to specify where 
# Spark is stored (this is dependent on the source 
# image)
ENV SPARK_HOME=/spark
ENV PATH="${SPARK_HOME}/bin:${PATH}"
ENV PY4J_VERSION=0.10.6
ENV PYTHONPATH="${SPARK_HOME}/python/lib/py4j-${PY4J_VERSION}-src.zip:${SPARK_HOME}/python/lib/pyspark.zip"


#####################################################
# Update to Python 3 and install relevant packages 

# Install jupyter 
RUN . /root/.bashrc && \
    pip install jupyter&& \
    pip install --upgrade jupyter-client

#####################################################
# Install Scala

ENV SCALA_VERSION=2.11.12

RUN apt-get update && \
    apt-get install -y libjansi-java && \
    wget https://downloads.lightbend.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.deb -O /tmp/scala.deb && dpkg -i /tmp/scala.deb && rm -rf /tmp/scala.deb && \ 
    apt-get clean


#####################################################
# Install Nodejs
ENV NVM_DIR=/usr/local/nvm 
ENV NODE_VERSION=10.6.0

# Install nvm with node and npm
RUN mkdir -p $NVM_DIR && \
    curl https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

ENV NODE_PATH="${NVM_DIR}/v${NODE_VERSION}/lib/node_modules"
ENV PATH="${NVM_DIR}/v${NODE_VERSION}/bin:${PATH}"


#####################################################
# Install PhotonML

RUN mkdir -p /usr/lib && \
    cd /usr/lib && \
    git clone https://github.com/linkedin/photon-ml.git && \
    cd photon-ml && \
    sed -i -E s/"defaultScalaVersion '.*'"/"defaultScalaVersion '${SCALA_VERSION}'"/ settings.gradle && \
    sed -i -E s/"targetScalaVersions '.*'"/"targetScalaVersions '${SCALA_VERSION}'"/ settings.gradle && \
    ./gradlew assemble

ENV PHOTONML_DIR=/usr/lib/photon-ml 


#####################################################
# Install Mahout

ENV MAHOUT_VERSION=0.13.0
RUN mkdir -p /usr/lib && \
    wget -O /usr/lib/mahout.tar.gz http://www-eu.apache.org/dist/mahout/${MAHOUT_VERSION}/apache-mahout-distribution-${MAHOUT_VERSION}.tar.gz && \
    cd /usr/lib/ && \
    tar -zxvf /usr/lib/mahout.tar.gz && \
    mv apache-mahout-distribution-${MAHOUT_VERSION} /usr/lib/mahout

ENV MAHOUT_HOME=/usr/lib/mahout
ENV MAHOUT_LOCAL=true
ENV PATH="${MAHOUT_HOME}/bin:${PATH}"


#####################################################
# Install recommendation / machine learning libraries 

RUN . /root/.bashrc && \
    pip install numpy scipy cython requests && \
    pip install sklearn lightfm scikit-surprise && \
    pip install nltk tensorflow && \
    pip install http://download.pytorch.org/whl/cpu/torch-0.4.0-cp36-cp36m-linux_x86_64.whl && \
    pip install torchvision && \ 
    pip install msgpack msgpack-numpy dvc datmo && \
    pip install keras gensim nimfa tensorrec avro && \
    cd /tmp && git clone https://github.com/maciejkula/spotlight.git && cd /tmp/spotlight && \
    python setup.py install && cd /tmp && rm -rf /tmp/spotlight && \
    npm install -g ger hapiger

# Entrypoint
RUN mkdir -p /work
WORKDIR /work
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]