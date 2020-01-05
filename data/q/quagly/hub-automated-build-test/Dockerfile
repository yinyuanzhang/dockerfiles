FROM jupyter/all-spark-notebook
LABEL maintainer="Michael West <quagly@gmail.com>"

USER root

RUN  apt-get -y update && \
     apt-get install --no-install-recommends -y vim &&\
     rm -rf /var/lib/apt/lists/*

USER jovyan

ENV PATH $PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

# if I keep logging into the container then consider adding ${HOME} setup here
