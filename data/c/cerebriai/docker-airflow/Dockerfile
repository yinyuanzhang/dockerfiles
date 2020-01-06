# VERSION 1.10.2
# AUTHOR: Matthieu "Puckel_" Roisil
# DESCRIPTION: Basic Airflow container
# BUILD: docker build --rm -t puckel/docker-airflow .
# SOURCE: https://github.com/puckel/docker-airflow

FROM cerebriai/spark:v2.4.3 as spark
RUN echo "In stage spark" \
    && ls -la /opt/spark

FROM adoptopenjdk/openjdk8:slim as openjdk
RUN echo "In stage openjdk" \
    && ls -la /opt/java/openjdk

ENV HADOOP_VERSION 3.2.0
FROM cerebriai/hadoop:3.2.0 as hadoop
RUN echo "In stage hadoop" \
    && ls -la /opt/hadoop-$HADOOP_VERSION

FROM python:3.6-slim
LABEL maintainer="nic@cerebriai.com"

# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

# Airflow
ARG AIRFLOW_VERSION=1.10.2
ARG AIRFLOW_HOME=/usr/local/airflow
ARG AIRFLOW_DEPS="kubernetes"
ARG PYTHON_DEPS="tornado<6.0.0 redis psycopg2-binary hdfs"
ENV AIRFLOW_GPL_UNIDECODE yes

# Define en_US.
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8

# Java
COPY --from=openjdk /opt/java/openjdk /opt/java/openjdk
ENV JAVA_HOME=/opt/java/openjdk
ENV PATH=$PATH:${JAVA_HOME}/bin
RUN echo "In stage airflow" \
    && java -version

# Spark
COPY --from=spark /opt/spark /opt/spark
COPY --from=spark /dependencies/ /dependencies
ENV SPARK_HOME /opt/spark
ENV PATH=$PATH:${SPARK_HOME}/bin
RUN echo "In stage airflow" \
    && spark-submit --version

# Hadoop
ENV HADOOP_VERSION 3.2.0
COPY --from=hadoop /opt/hadoop-$HADOOP_VERSION /opt/hadoop-$HADOOP_VERSION
ENV HADOOP_HOME=/opt/hadoop-$HADOOP_VERSION
ENV HADOOP_CLASSPATH=$HADOOP_CLASSPATH:/opt/hadoop-$HADOOP_VERSION/share/hadoop/tools/lib/*
ENV HADOOP_CONF_DIR=/etc/hadoop
ADD core-site.xml /etc/hadoop/core-site.xml
ADD hdfs-site.xml /etc/hadoop/hdfs-site.xml
ENV HADOOP_OPTIONAL_TOOLS=hadoop-azure
ENV MULTIHOMED_NETWORK=1
ENV PATH=$PATH:$HADOOP_HOME/bin

COPY config/log4j.properties ${HADOOP_CONF_DIR}/log4j.properties

RUN set -ex \
    && buildDeps=' \
        freetds-dev \
        libkrb5-dev \
        libsasl2-dev \
        libssl-dev \
        libffi-dev \
        libpq-dev \
        git \
    ' \
    && apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends \
        $buildDeps \
        freetds-bin \
        build-essential \
        default-libmysqlclient-dev \
        apt-utils \
        curl \
        rsync \
        netcat \
        locales \
        nano \
        vim \
        sudo \
        bzip2 \
        unzip \
    && sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \
    && locale-gen "en_US.UTF-8" \
    && dpkg-reconfigure locales \
    && update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \
    && useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow \
    ## adding sudo to airflow user
    && echo 'airflow ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/user \
    && chmod 0440 /etc/sudoers.d/user \
    && usermod -aG sudo airflow \
    && su - airflow -c "touch mine" \
    && pip install -U pip setuptools wheel \
    && pip install pytz \
    && pip install pyOpenSSL \
    && pip install ndg-httpsclient \
    && pip install pyasn1 \
    && pip install apache-airflow[crypto,celery,hdfs,postgres,hive,jdbc,mysql,ssh${AIRFLOW_DEPS:+,}${AIRFLOW_DEPS}]==${AIRFLOW_VERSION} \
#    && pip install 'redis>=2.10.5,<3' \
    && pip install elasticsearch-dsl==6.4.0 \
    && if [ -n "${PYTHON_DEPS}" ]; then pip install ${PYTHON_DEPS}; fi \
    && apt-get purge --auto-remove -yqq $buildDeps \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man \
        /usr/share/doc \
        /usr/share/doc-base

COPY script/entrypoint.sh /entrypoint.sh
COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg

# LDAP
RUN echo -n | openssl s_client -host 10.1.0.7 -port 636 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > /tmp/cerebri.com.crt
COPY config/webserver_config.py ${AIRFLOW_HOME}/webserver_config.py

RUN chown -R airflow: ${AIRFLOW_HOME}

EXPOSE 8080 5555 8793

USER airflow
WORKDIR ${AIRFLOW_HOME}
ENTRYPOINT ["/entrypoint.sh"]
CMD ["webserver"] # set default arg for entrypoint
