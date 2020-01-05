FROM rocker/r-ubuntu:18.04

RUN apt-get clean

# RSTUDIO and RJava
#####################################################################
RUN export DEBIAN_FRONTEND=noninteractive \
  && apt-get update \
  && apt-get install -y --no-install-recommends gdebi-core openjdk-8-jdk git \
       libapparmor1 sudo libcurl4-openssl-dev libssl1.0.0 libclang-dev

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV SPARK_VERSION=2.4.4
ENV HADOOP_VERSION=2.7
ENV SCALA_VERSION=2.11.12
ENV POLYNOTE_VERSION=0.2.11

ENV SPARK_HOME=/opt/spark
ENV PATH="/opt/conda/bin:/usr/lib/rstudio-server/bin:$JAVA_HOME/bin:$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin"

RUN export DEBIAN_FRONTEND=noninteractive \ 
  && wget https://download2.rstudio.org/server/bionic/amd64/rstudio-server-1.2.5019-amd64.deb \
  && gdebi -n rstudio-server-1.2.5019-amd64.deb \
  && rm /etc/environment && touch /etc/environment \
  && echo "JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> /etc/environment \
  && /bin/bash -c "source /etc/environment" \
  && R CMD javareconf \
  && Rscript -e "install.packages('rJava')" \
  && rm rstudio-server-1.2.5019-amd64.deb \
  && echo "PATH=${PATH}" >> /etc/environment \
  && echo "PATH=${PATH}" >> /etc/R/Renviron \
  && echo "SPARK_HOME=${SPARK_HOME}" >> /etc/R/Renviron \
  && echo "JAVA_HOME=${JAVA_HOM}" >> /etc/R/Renviron

# rocker
RUN export DEBIAN_FRONTEND=noninteractive \
  && useradd rstudio \
  && echo "rstudio:rstudio" | chpasswd \
	&& mkdir /home/rstudio \
	&& chown rstudio:rstudio /home/rstudio \
	&& addgroup rstudio staff

RUN export DEBIAN_FRONTEND=noninteractive \
  && apt-get update \
  && apt-get install -y --no-install-recommends libxml2-dev libssl-dev \
  && Rscript -e "install.packages('devtools')" \
  && Rscript -e "install.packages('tidyverse')" \
  && Rscript -e "install.packages('data.table')"

# INIT Config
##############################################################################
# https://github.com/QuantumObject/docker-baseimage/blob/master/system_services.sh
## Fix some issues with APT packages.
## See https://github.com/dotcloud/docker/issues/1024
RUN dpkg-divert --local --rename --add /sbin/initctl \
  && ln -sf /bin/true /sbin/initctl

ENV INITRD=no
RUN mkdir -p /etc/container_environment && echo -n no > /etc/container_environment/INITRD

## Install init process.
COPY my_init /sbin/my_init 
RUN chmod 750 /sbin/my_init   \
  && mkdir -p /etc/my_init.d && mkdir -p /etc/container_environment  \
  && touch /etc/container_environment.sh && touch /etc/container_environment.json  \
  && chmod 700 /etc/container_environment

RUN locale-gen en_US.UTF-8 \
  && update-locale LANG=en_US.UTF-8 LC_CTYPE=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8 \
  && echo -n en_US.UTF-8 > /etc/container_environment/LANG  \
  && echo -n en_US.UTF-8 > /etc/container_environment/LC_CTYPE \
  && echo -n en_US:en > /etc/container_environment/LANGUAGE  \
  && echo -n en_US.UTF-8 > /etc/container_environment/LC_ALL

RUN groupadd -g 8377 docker_env \
  && chown :docker_env /etc/container_environment.sh /etc/container_environment.json \
  && chmod 640 /etc/container_environment.sh /etc/container_environment.json \
  && ln -s /etc/container_environment.sh /etc/profile.d/ \
  && echo ". /etc/container_environment.sh" >> /root/.bashrc

## Install runit.
RUN export DEBIAN_FRONTEND=noninteractive \
  && apt-get update \
  && apt-get install -y --no-install-recommends runit cron

## Install cron daemon.
RUN mkdir -p /etc/service/cron && mkdir -p /var/log/cron \
  && chmod 600 /etc/crontab
COPY runit/cron /etc/service/cron/run 
COPY cron_config/cron_log_config /var/log/cron/config 
RUN chown -R nobody  /var/log/cron && chmod +x /etc/service/cron/run

#############################################################################
# https://github.com/QuantumObject/docker-rstudio
##startup scripts: Pre-config when the container run the first time
RUN mkdir -p /etc/my_init.d
COPY startup.sh /etc/my_init.d/startup.sh
RUN chmod +x /etc/my_init.d/startup.sh

##Adding Deamons to containers
RUN mkdir /etc/service/rserver /var/log/rserver ; sync
COPY rserver.sh /etc/service/rserver/run
RUN chmod +x /etc/service/rserver/run \
    && cp /var/log/cron/config /var/log/rserver/ \
    && chown -R rstudio-server /var/log/rserver

RUN (adduser --disabled-password --gecos "" guest && echo "guest:guest"|chpasswd)

# Scala and Spark
################################################################################

RUN wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
  && tar -zxvf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
  && mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} spark \
  && mv spark /opt/spark \
  && rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

RUN wget -O- "https://www.scala-lang.org/files/archive/scala-${SCALA_VERSION}.tgz" \
    | tar xzf - -C /usr/local --strip-components=1

# Python
#######################################################################
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.5.4-Linux-x86_64.sh -O ~/miniconda.sh \
  && /bin/bash ~/miniconda.sh -b -p /opt/conda && rm ~/miniconda.sh

RUN ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh \
  && echo "source /etc/environment" >> /etc/my_init.d/startup.sh \
  && echo ". /opt/conda/etc/profile.d/conda.sh" >> /etc/my_init.d/startup.sh \
  && echo "conda activate base" >> /etc/my_init.d/startup.sh

# Cleaning
#############################################################################
RUN export DEBIAN_FRONTEND=noninteractive \
  && apt-get clean \
  && rm -rf /tmp/* \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get autoremove -y \
  && apt-get autoclean -y \
  && apt-get update

# to allow access from outside of the container to the container service
# at that ports need to allow access from firewall if need to access it outside of the server.
EXPOSE 8787
##############################################################################
CMD ["/sbin/my_init"]
