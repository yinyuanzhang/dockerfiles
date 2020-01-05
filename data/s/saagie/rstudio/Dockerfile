FROM rocker/tidyverse:3.4.2

USER root

# Spark dependencies versions
ENV APACHE_SPARK_VERSION 2.1.0
ENV HADOOP_VERSION 2.7

# Install system libraries required by R packages
RUN apt-get -y update  && apt-get install -y libcups2 libcups2-dev openjdk-8-jdk systemd \
    unixodbc-dev libbz2-dev libgsl-dev odbcinst libx11-dev mesa-common-dev libglu1-mesa-dev \
    gdal-bin proj-bin libgdal-dev libproj-dev libudunits2-dev libtcl8.6 libtk8.6 libgtk2.0-dev && \
    apt-get clean

# Install Impala ODBC dependency
RUN cd /tmp && \
    wget --no-verbose https://downloads.cloudera.com/connectors/impala_odbc_2.5.41.1029/Debian/clouderaimpalaodbc_2.5.41.1029-2_amd64.deb && \
    dpkg -i clouderaimpalaodbc_2.5.41.1029-2_amd64.deb && \
    odbcinst -i -d -f /opt/cloudera/impalaodbc/Setup/odbcinst.ini

# Install Spark
RUN cd /tmp && \
    wget -q https://archive.apache.org/dist/spark/spark-${APACHE_SPARK_VERSION}/spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    tar xzf spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C /usr/local && \
    rm spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} spark

# Mesos dependencies
RUN DISTRO=debian && \
    CODENAME=stretch && \
    echo "deb http://repos.mesosphere.io/${DISTRO} ${CODENAME} main" > /etc/apt/sources.list.d/mesosphere.list && \
    apt-get -y update && \
    apt-get --no-install-recommends -y --force-yes install mesos=1.3.1-2.0.1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Spark and Mesos config
ENV SPARK_HOME /usr/local/spark
ENV MESOS_NATIVE_LIBRARY /usr/local/lib/libmesos.so
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info

RUN R -e "install.packages('sparklyr', repos='http://cran.rstudio.com/', dependencies=T)"

# Install Saagie's RStudio Addin
RUN R -e "install.packages('devtools')" && \
  R -e "devtools::install_github('saagie/rstudio-saagie-addin')"

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

# Install R packages
RUN R CMD javareconf && R -e "install.packages('rJava')" && \
 R -e "install.packages('odbc')" && \
 R -e "install.packages('RJDBC')" && \
 R -e "install.packages('implyr')" && \
 R -e "install.packages('futile.logger')" && \
 R -e "install.packages('h2o')" && \
 R -e "install.packages('caret')" && \
 R -e "install.packages('ROSE')" && \
 R -e "install.packages('caretEnsemble')" && \
 R -e "install.packages('randomForest')" && \
 R -e "install.packages('pROC')" && \
 R -e "install.packages('rsparkling')" && \
 R -e "install.packages('xts')" && \
 R -e "install.packages('dygraphs')" && \
 R -e "install.packages('forecast')" && \
 R -e "install.packages('mclust')" && \
 R -e "install.packages('factoextra')" && \
 R -e "install.packages('dbscan')" && \
 R -e "install.packages('dtw')" && \
 R -e "install.packages('ROCR')" && \
 R -e "install.packages('Rtsne')" && \
 R -e "install.packages('corrplot')" && \
 R -e "install.packages('dummies')" && \
 R -e "install.packages('xgboost')" && \
 R -e "install.packages('e1071')" && \
 R -e "install.packages('DescTools')" && \
 R -e "install.packages('packrat')" && \
 R -e "install.packages('tm')" && \
 R -e "install.packages('RTextTools')" && \
 R -e "install.packages('networkD3')" && \
 R -e "install.packages('sqldf')" && \
 R -e "install.packages('syuzhet')" && \
 R -e "install.packages('TSclust')" && \
 R -e "install.packages('arules')" && \
 R -e "install.packages('arulesSequences')" && \
 R -e "install.packages('recommenderlab')" && \
 R -e "install.packages('AUC')" && \
 R -e "install.packages('kohonen')" && \
 R -e "install.packages('topicmodels')" && \
 R -e "install.packages('argparse')" && \
 R -e "install.packages('lsa')" && \
 R -e "install.packages('d3heatmap')" && \
 R -e "install.packages('pvclust')" && \
 R -e "install.packages('trend')" && \
 R -e "install.packages('breakpoint')" && \
 R -e "install.packages('changepoint')" && \
 R -e "install.packages('mvoutlier')" && \
 R -e "install.packages('shinydashboard')" && \
 R -e "install.packages('FNN')" && \
 R -e "install.packages('plotly')" && \
 R -e "install.packages('RMySQL')" && \
 R -e "install.packages('DescTools')" && \
 R -e "install.packages('doParallel')" && \
 R -e "install.packages('ff')" && \
 R -e "install.packages('ffbase')" && \
 R -e "install.packages('jsonlite')" && \
 R -e "install.packages('forecast')" && \
 R -e "install.packages('tseries')" && \
 R -e "install.packages('trend')" && \
 R -e "install.packages('rvest')" && \
 R -e "install.packages('curl')" && \
 R -e "install.packages('RSelenium')" && \
 R -e "install.packages('Rcpp')" && \
 R -e "install.packages('ggplot2')" && \
 R -e "install.packages('rpart.plot')" && \
 R -e "install.packages('labeling')" && \
 R -e "install.packages('reshape2')" && \
 R -e "install.packages('shiny')" && \
 R -e "install.packages('markdown')" && \
 R -e "install.packages('shinydashboard')" && \
 R -e "install.packages('knitr')" && \
 R -e "install.packages('shinyjs')" && \
 R -e "install.packages('shinythemes')" && \
 R -e "install.packages('dtplyr')" && \
 R -e "install.packages('stringr')" && \
 R -e "install.packages('data.table')" && \
 R -e "install.packages('xlsx')" && \
 R -e "install.packages('sas7bdat')" && \
 R -e "install.packages('readxl')" && \
 R -e "install.packages('readr')" && \
 R -e "install.packages('rjson')" && \
 R -e "install.packages('leaflet')" && \
 R -e "install.packages('RColorBrewer')" && \
 R -e "install.packages('classInt')" && \
 R -e "install.packages('maptools')" && \
 R -e "install.packages('colorspace')" && \
 R -e "install.packages('colourpicker')" && \
 R -e "install.packages('mapproj')" && \
 R -e "install.packages('maps')" && \
 R -e "install.packages('scales')" && \
 R -e "install.packages('sp')" && \
 R -e "install.packages('FactoMineR')" && \
 R -e "install.packages('FactoInvestigate')" && \
 R -e "install.packages('missMDA')" && \
 R -e "install.packages('RcmdrMisc')" && \
 R -e "install.packages('ade4')" && \
 R -e "install.packages('RTextTools')" && \
 R -e "install.packages('tree')" && \
 R -e "install.packages('kknn')" && \
 R -e "install.packages('kernlab')" && \
 R -e "install.packages('rpart')" && \
 R -e "install.packages('e1071')" && \
 R -e "install.packages('randomForest')" && \
 R -e "install.packages('pls')" && \
 R -e "install.packages('betareg')" && \
 R -e "install.packages('glmnet')" && \
 R -e "install.packages('leaps')" && \
 R -e "install.packages('mlogit')" && \
 R -e "install.packages('pROC')" && \
 R -e "install.packages('caret')" && \
 R -e "install.packages('wordcloud')" && \
 R -e "install.packages('stringi')" && \
 R -e "install.packages('SnowballC')" && \
 R -e "install.packages('RWeka')" && \
 R -e "install.packages('hunspell')" && \
 R -e "install.packages('topicmodels')" && \
 R -e "install.packages('magrittr')" && \
 R -e "install.packages('cluster')" && \
 R -e "install.packages('proxy')" && \
 R -e "install.packages('skmeans')" && \
 R -e "install.packages('LDAvis')" && \
 R -e "install.packages('lsa')" && \
 R -e "install.packages('doSNOW')" && \
 R -e "install.packages('cartography')" && \
 R -e "install.packages('Factoshiny')" && \
 R -e "install.packages('cairoDevice', INSTALL_opts='--no-test-load')" && \
 R -e "install.packages('rattle')"

RUN mkdir /root/.R/
RUN echo CXXFLAGS=-DBOOST_PHOENIX_NO_VARIADIC_EXPRESSION > /root/.R/Makevars
RUN R -e "install.packages('prophet')"

# Be sure rstudio user has full access to his home directory
RUN mkdir -p /home/rstudio && \
  chown -R rstudio:rstudio /home/rstudio && \
  chmod -R 755 /home/rstudio

ADD ./init_rstudio.sh /
RUN chmod 500 /init_rstudio.sh

# JAVA_HOME define
ENV PATH=$JAVA_HOME/bin:$PATH

# Hadoop client installation
RUN wget --no-verbose http://archive-primary.cloudera.com/cdh5/cdh/5/hadoop-2.6.0-cdh5.7.1.tar.gz \
&& tar -xzf hadoop-2.6.0-cdh5.7.1.tar.gz \
&& rm hadoop-2.6.0-cdh5.7.1.tar.gz \
&& mv hadoop-2.6.0-cdh5.7.1 /usr/local/hadoop
ENV HADOOP_HOME=/usr/local/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin

# Hive client installation
RUN wget --no-verbose http://apache.mirrors.ovh.net/ftp.apache.org/dist/hive/hive-1.2.2/apache-hive-1.2.2-bin.tar.gz \
&& tar -xvzf apache-hive-1.2.2-bin.tar.gz \
&& rm apache-hive-1.2.2-bin.tar.gz \
&& cd apache-hive-1.2.2-bin
ENV HIVE_HOME=/apache-hive-1.2.2-bin
ENV PATH=/apache-hive-1.2.2-bin/bin:$PATH


CMD ["/bin/sh", "-c", "/init_rstudio.sh"]
