FROM debian:8

# install basic packages
RUN apt-get update --fix-missing && \
  apt-get -y upgrade && \
  apt-get install -y curl git man bzip2 ca-certificates unzip vim wget && \
  apt-get install -y software-properties-common  

# install java
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd8team-java.list && \
  echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list && \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && \
  apt-get update -y && \
  apt-get upgrade -y && \
  echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections && \
  apt-get install -y oracle-java8-installer -f

WORKDIR /home

# install spark
RUN wget --quiet https://archive.apache.org/dist/spark/spark-2.1.3/spark-2.1.3-bin-hadoop2.7.tgz && \
    tar -zxvf spark-2.1.3-bin-hadoop2.7.tgz && \
    mv spark-2.1.3-bin-hadoop2.7 /usr/local/spark

ENV PATH /usr/local/spark/bin:$PATH
ENV SPARK_HOME=/usr/local/spark/ 
ENV PYTHONPATH=$SPARK_HOME/python/:$SPARK_HOME/python/lib/py4j-0.10.7-src.zip:$PYTHONPATH

# install Python 3.5.2
RUN apt-get update && \
  apt-get install -y make build-essential libssl-dev zlib1g-dev && \
  apt-get install -y libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm && \
  apt-get install -y libncurses5-dev  libncursesw5-dev xz-utils tk-dev

RUN wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz && \
  tar xvf Python-3.5.2.tgz && \
  cd Python-3.5.2 && \
  ./configure --enable-optimizations && \
  make -j8 && \
  make altinstall

# install pyenv and pipenv
RUN curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash && \
  export PATH="/root/.pyenv/bin:$PATH" && \
  eval "$(pyenv init -)" && \
  eval "$(pyenv virtualenv-init -)" && \
  pyenv update

RUN apt-get install -y python-pip && \
  pip install pipenv

CMD ["bash"]
