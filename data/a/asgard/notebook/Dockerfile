FROM jupyter/scipy-notebook:c33a7dc0eece

USER root

# lxml
RUN apt-get update && apt-get install -y libxml2-dev libxslt1-dev python-lxml curl libssl-dev

# install python packages +. spacy models
ADD ./py-requirement.txt py-requirement.txt
RUN pip2 install --upgrade pip && pip2 install -U -r py-requirement.txt

# instal jdk 8
RUN echo 'deb http://cdn-fastly.deb.debian.org/debian jessie-backports main' > /etc/apt/sources.list.d/jessie-backports.list && \
    apt-get -y update && \
    apt-get install --no-install-recommends -t jessie-backports -y openjdk-8-jre-headless ca-certificates-java && \
    rm /etc/apt/sources.list.d/jessie-backports.list && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install spark
ARG SPARK_VERSION=2.1.1
ARG HADOOP_VERSION=2.7
ENV SPARK_PACKAGE $SPARK_VERSION-bin-hadoop$HADOOP_VERSION
ENV SPARK_HOME /usr/local/spark-$SPARK_PACKAGE
ENV PATH $PATH:$SPARK_HOME/bin
RUN curl -sL --retry 3 \
  "http://www-eu.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_PACKAGE.tgz" \
  | sudo gunzip \
  | sudo tar x -C /usr/local \
  && sudo ln -s $SPARK_HOME /usr/local/spark

# ADD several jars for S3 connection, mysql...
RUN mkdir -p $SPARK_HOME/jars \
  && wget -P $SPARK_HOME/jars \
    "http://central.maven.org/maven2/com/amazonaws/aws-java-sdk/1.7.4/aws-java-sdk-1.7.4.jar" \
    "http://central.maven.org/maven2/org/apache/hadoop/hadoop-aws/2.7.1/hadoop-aws-2.7.1.jar" \
    "http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.38/mysql-connector-java-5.1.38.jar"

# add spark-conf
# ADD ./spark-defaults.conf $SPARK_HOME/conf/spark-defaults.conf
ADD ./hdfs-site.xml $SPARK_HOME/conf/hdfs-site.xml
RUN cp $SPARK_HOME/conf/log4j.properties.template $SPARK_HOME/conf/log4j.properties

# Spark and Mesos config
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.4-src.zip

# Clean up APT when done.
RUN apt-get clean  \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER $NB_USER

# install jupyter extension and configurator
# custom to fix issue with snippets
RUN git clone https://github.com/thomasopsomer/jupyter_contrib_nbextensions.git \
  && pip install -e jupyter_contrib_nbextensions \
  && jupyter contrib nbextension install --user \
  && rm -r jupyter_contrib_nbextensions \
  && jupyter nbextension enable snippets/main \
  && jupyter nbextension enable codefolding/main \
  && jupyter nbextension enable tree-filter/index \
  && jupyter nbextension enable snippets_menu/main \
  && jupyter nbextension enable varInspector/main \
  && jupyter nbextension enable comment-uncomment/main \
  && conda install -y -c conda-forge jupyter_nbextensions_configurator

# install jupyter spark plugin from mozilla
RUN pip install jupyter-spark && \
  jupyter serverextension enable --py jupyter_spark && \
  jupyter nbextension install --user --py jupyter_spark && \
  jupyter nbextension enable --py jupyter_spark && \
  jupyter nbextension enable --py widgetsnbextension

# add code snippets
ADD snippets.json /home/$NB_USER/.local/share/jupyter/nbextensions/snippets/snippets.json

EXPOSE 4040




