FROM ubuntu:16.04
LABEL maintainer="alessandrov87 (https://github.com/AlessandroVaccarino)"

ENV DRILL_VERSION 1.13.0

# Install dev tools
RUN apt-get update && apt-get install -y wget tar sudo && rm -rf /var/lib/apt/lists/*

# Install java8
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y  software-properties-common && \
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update && \
    echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer && \
    apt-get clean

# Create Drill folder
RUN mkdir -p /opt/drill

# Download Drill
RUN wget -O /opt/drill/apache-drill.tar.gz http://it.apache.contactlab.it/drill/drill-$DRILL_VERSION/apache-drill-$DRILL_VERSION.tar.gz

# Extract Drill from tar.gz and delete downloaded file
RUN tar -xvzf /opt/drill/apache-drill.tar.gz -C /opt/drill
RUN rm /opt/drill/apache-drill.tar.gz

# add boostrap.sh file, with Drill launcher
ADD bootstrap.sh /etc/bootstrap.sh
RUN chown root:root /etc/bootstrap.sh
RUN chmod 700 /etc/bootstrap.sh
ENV BOOTSTRAP /etc/bootstrap.sh

# Expose ports
EXPOSE 8047
EXPOSE 31010
