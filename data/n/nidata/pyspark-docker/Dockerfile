FROM debian

RUN apt-get update

# Install python3 and java
RUN apt-get -y install wget default-jdk python3.5 python-dev build-essential python3-pip
RUN easy_install3 -U pip

# locked version of setuptools on purpose, otherwise it crash
RUN pip3 install --ignore-installed setuptools==33.1.1 google-cloud google-api-python-client pytz pyyaml docopt pytest pyspark jsondiff --user

# Install spark
RUN wget http://apache.lauf-forum.at/spark/spark-2.3.1/spark-2.3.1-bin-hadoop2.7.tgz
RUN tar -xzvf spark-2.3.1-bin-hadoop2.7.tgz
RUN rm spark-2.3.1-bin-hadoop2.7.tgz
RUN mv spark-2.3.1-bin-hadoop2.7 spark
RUN mv spark/conf/spark-env.sh.template spark/conf/spark-env.sh
RUN mv spark/conf/spark-defaults.conf.template spark/conf/spark-defaults.conf
RUN mv spark/ /usr/lib/

# Spark conf
RUN echo "export JAVA_HOME=/usr/lib/jvm/default-java/jre" >> ~/.bashrc
RUN echo "export SPARK_HOME=/root/.local/lib/python3.5/site-packages/pyspark" >> ~/.bashrc
RUN echo "export PATH=SPARK_HOME/bin:$PATH" >> ~/.bashrc
RUN echo "export PYSPARK_PYTHON=python3" >> ~/.bashrc
RUN echo "export PYTHONHASHSEED=0" >> /usr/lib/spark/conf/spark-env.sh
RUN echo "spark.executorEnv.PYTHONHASHSEED=0" >> /usr/lib/spark/conf/spark-defaults.conf
RUN echo "spark.sql.caseSensitive=true" >> /usr/lib/spark/conf/spark-defaults.conf
