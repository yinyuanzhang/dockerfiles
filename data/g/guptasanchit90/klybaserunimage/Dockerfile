FROM centos

# Install required dependencies
RUN yum install -yy curl wget sudo unzip mariadb git

# Download spark
RUN mkdir -p /opt/spark
RUN wget http://apache.crihan.fr/dist/spark/spark-2.3.1/spark-2.3.1-bin-hadoop2.7.tgz
RUN tar zxvf spark-2.3.1-bin-hadoop2.7.tgz -C /opt/spark && rm -f spark-2.3.1-bin-hadoop2.7.tgz

# Install wait-for-it
RUN cd /opt && git clone https://github.com/vishnubob/wait-for-it.git